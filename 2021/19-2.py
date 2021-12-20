from itertools import combinations as comb, permutations as perm, product
import numpy as np

# Read scanners detections
scans = []
next_scan = []

try:
    while True:
        line = input()

        if line.startswith("---"):
            if next_scan:
                scans.append(next_scan)
                next_scan = []
        elif line:
            next_scan.append(np.array(list(map(int, line.split(","))) + [1,]))
except EOFError:
    pass

scans.append(next_scan)

# Enumerate all 3D homogeneous permutation matrices
def perm_mats():
    for x, y, z in perm(range(3)):
        result = np.zeros((4, 4), dtype=int)
        result[(x, y, z, 3), range(4)] = 1
        yield result

# Find a rigid transformation between two pairs of points, if it exists
def find_pose(p1, q1, p2, q2):
    for mat in perm_mats():
        num = p1[:3] - p2[:3]
        den = (mat @ q1)[:3] - (mat @ q2)[:3]

        if (den == 0).any(): continue
        if (num % den != 0).any(): continue

        s = num // den

        if ((s != -1) & (s != 1)).any(): continue

        t = (mat @ q1)[:3] - s * p1[:3]

        return mat.T @ np.array([
            [s[0], 0, 0, t[0]],
            [0, s[1], 0, t[1]],
            [0, 0, s[2], t[2]],
            [0, 0, 0, 1],
        ])

# Try to orient scanner #j relative to any other already-oriented scanner
def orient(j, poses):
    for i in poses:
        for pi, pj in product(comb(scans[i], 2), comb(scans[j], 2)):
            pose = find_pose(pj[0], pi[0], pj[1], pi[1])

            if pose is not None:
                pj_from_pi = pose @ np.stack(scans[j]).T
                pj_points = set([tuple(row[:3]) for row in pj_from_pi.T])
                pi_points = set([tuple(row[:3]) for row in scans[i]])
                shared = pi_points & pj_points

                if len(shared) >= 12:
                    poses[j] = poses[i] @ pose
                    print(f"Oriented from {i}:")
                    print(poses[j])
                    return True

    return False

# Orient all scanners relative to scanner #0
def orient_all():
    poses = {}
    remaining = set(range(len(scans)))

    poses[0] = np.eye(4, dtype=int)
    remaining.remove(0)

    while remaining:
        print("Remains to orient: ", remaining)

        for j in remaining.copy():
            print(f"Orienting {j}...")

            if orient(j, poses):
                remaining.remove(j)
            else:
                print("Failed")

    return poses

poses = orient_all()
print(max(
    np.abs(p1[:, 3] - p2[:, 3]).sum()
    for p1, p2 in product(poses.values(), repeat=2)
))
