class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

## C++ version By @Yoursong 
class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        def func_gcd(a, b):
            if b == 0:
                return a
            else:
                return func_gcd(b, a % b)
        num_points = len(points)
        if num_points < 2:
            return num_points
        
        max_points = 0
        for i in range(num_points):
            lines = {}
            tmp_max, same, ver = 0, 0, 0
            for j in range(i+1, num_points):
                if points[j].x == points[i].x and points[j].y == points[i].y:
                    same += 1
                    continue
                elif points[j].x == points[i].x:
                    ver += 1
                else:
                    dx = points[i].x - points[j].x
                    dy = points[i].y - points[j].y
                    gcd = func_gcd(dx, dy)
                    dx, dy = dx / gcd, dy / gcd
                    if (dx, dy) not in lines:
                        lines[(dx, dy)] = 1
                    else:
                        lines[(dx, dy)] += 1
                    tmp_max = max(lines[(dx, dy)], tmp_max)
                tmp_max = max(ver, tmp_max)
            max_points = max(max_points, tmp_max + same + 1)
        return max_points
                    
class Solution0:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        MIN_VALUE = -10000000000
        MAX_VALUE = 10000000000
        if points == None or len(points) == 0:
            return 0

        dmap = {}
        maxi = 1
        for i in range(len(points)):
            dmap = {}
            dmap[MIN_VALUE] = 1

            dup = 0
            for j in range(i+1, len(points)):
                if points[j].x == points[i].x and points[j].y == points[i].y:
                    dup += 1
                    continue

                if points[j].x - points[i].x == 0:
                    key = MAX_VALUE
                else:
                    key = (points[j].y - points[i].y) / (points[j].x - points[i].x)

                if key in dmap:
                    dmap[key] += 1
                else:
                    dmap[key] = 2

            for k in dmap.keys():
                if dmap[k] + dup > maxi:
                    maxi = dmap[k] + dup
        return maxi
                        

class Solution1:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        
        
        def inaline(p, l):
            p1, p2 = l
            dx1 = float(p1[0] - p2[0])
            dy1 = float(p1[1] - p2[1])

            dx2 = float(p1[0] - p[0])
            dy2 = float(p1[1] - p[1])

            if dy1 == 0.0 and dy2 == 0.0:
                return True
            elif dy1 != 0.0 and dy2 != 0.0:
                if dx1 / dy1 == dx2 / dy2:
                    return True
                else:
                    return False
            else:
                return False
            
        np = []
        for p in points:
            if (p.x, p.y) not in np:
                np.append((p.x, p.y))

        if len(np) == 1:
            return 1
        elif len(np) == 0:
            return 0
        elif len(np) == 2:
            return 2
        
        pairs = {}
        allline = []
        for p in np:
            for q in np:
                if p != q and ((q, p) not in pairs):
                    pairs[(p,q)] = 2

                    #for line in allline:
                    #    if (p in line) and (q in line):
                    #        continue
                    
                    tmpline = [p, q]
                    for m in np:
                        if m not in (p, q):
                            if inaline(m, (p, q)):
                                tmpline.append(m)

                    allline.append(tmpline)
                        
                                
        maxp = 2
        for line in allline:
            if len(line)> maxp:
                maxp = len(line)
        return maxp

class Solution2:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) == 1:
            return 1
        elif len(points) == 0:
            return 0
        elif len(points) == 2:
            return 2
            
        def inaline(p, l):
            p1, p2 = l
            dx1 = float(p1[0] - p2[0])
            dy1 = float(p1[1] - p2[1])

            dx2 = float(p1[0] - p[0])
            dy2 = float(p1[1] - p[1])

            if dy1 == 0.0 and dy2 == 0.0:
                return True
            elif dy1 != 0.0 and dy2 != 0.0:
                if dx1 / dy1 == dx2 / dy2:
                    return True
                else:
                    return False
            else:
                return False
            
        np = []
        for p in points:
            if (p.x, p.y) not in np:
                np.append((p.x, p.y))
        
        pairs = {}
        for p in np:
            for q in np:
                if p != q and ((q, p) not in pairs):
                    pairs[(p,q)] = 2

        for line in pairs.keys():
            for p in np:
                if p not in line:
                    if inaline(p, line):
                        pairs[line] += 1
        

        maxp = 2
        for line in pairs.keys():
            if pairs[line] > maxp:
                maxp = pairs[line]

        return maxp

class Solution3:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) == 1:
            return 1
        elif len(points) == 0:
            return 0
        elif len(points) == 2:
            return 2
            
        def inaline(p, l):
            p1, p2 = l
            dx1 = float(p1[0] - p2[0])
            dy1 = float(p1[1] - p2[1])

            dx2 = float(p1[0] - p[0])
            dy2 = float(p1[1] - p[1])

            if dy1 == 0.0 and dy2 == 0.0:
                return True
            elif dy1 != 0.0 and dy2 != 0.0:
                if dx1 / dy1 == dx2 / dy2:
                    return True
                else:
                    return False
            else:
                return False

        def tangtang(line):
            p1, p2 = line
            dx = float(p1[0] - p2[0])
            dy = float(p1[1] - p2[1])

            if dy == 0:
                return "I"
            else:
                return dx / dy
            
            
        np = []
        for p in points:
            if (p.x, p.y) not in np:
                np.append((p.x, p.y))
        
        pairs = {}
        pnum = {}
        pline = {}
        for p in np:
            for q in np:
                if p != q and ((q, p) not in pairs):
                    tang = tangtang((p, q))
                    nj = True
                    for line in pairs.keys():
                        if pairs[line] == tang:
                            if (p not in pline[line]):
                                pnum[line] += 1
                                pline[line].append(p)

                            if (q not in pline[line]):
                                pnum[line] += 1
                                pline[line].append(1)

                            nj = False
                            break

                    if nj:
                        pairs[(p,q)] = tang
                        pnum[(p,q)] = 2
                        pline[(p,q)] = [p,q]
        

        maxp = 2
        for line in pnum.keys():
            if pnum[line] > maxp:
                maxp = pnum[line]

        return maxp



import random
ps = []
a = [(560,248),(0,16),(30,250),(950,187),(630,277),(950,187),(-212,-268),(-287,-222),(53,37),(-280,-100),(-1,-14),(-5,4),(-35,-387),(-95,11),(-70,-13),(-700,-274),(-95,11),(-2,-33),(3,62),(-4,-47),(106,98),(-7,-65),(-8,-71),(-8,-147),(5,5),(-5,-90),(-420,-158),(-420,-158),(-350,-129),(-475,-53),(-4,-47),(-380,-37),(0,-24),(35,299),(-8,-71),(-2,-6),(8,25),(6,13),(-106,-146),(53,37),(-7,-128),(-5,-1),(-318,-390),(-15,-191),(-665,-85),(318,342),(7,138),(-570,-69),(-9,-4),(0,-9),(1,-7),(-51,23),(4,1),(-7,5),(-280,-100),(700,306),(0,-23),(-7,-4),(-246,-184),(350,161),(-424,-512),(35,299),(0,-24),(-140,-42),(-760,-101),(-9,-9),(140,74),(-285,-21),(-350,-129),(-6,9),(-630,-245),(700,306),(1,-17),(0,16),(-70,-13),(1,24),(-328,-260),(-34,26),(7,-5),(-371,-451),(-570,-69),(0,27),(-7,-65),(-9,-166),(-475,-53),(-68,20),(210,103),(700,306),(7,-6),(-3,-52),(-106,-146),(560,248),(10,6),(6,119),(0,2),(-41,6),(7,19),(30,250)]

for i in a:
    ps.append(Point(i[0], i[1]))


import time
#st = time.time()
#s = Solution1()
#print s.maxPoints(ps)
#et = time.time()
#print et - st


st = time.time()
s = Solution2()
print s.maxPoints(ps)
et = time.time()
print et - st


st = time.time()
s = Solution()
print s.maxPoints(ps)
et = time.time()
print et - st
