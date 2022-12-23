# _*_ coding=utf-8 _*_

import os
Path1 = '/home'
Path2 = '/develop'
Path3 = '/code'
Path10 = Path1 + Path2 + Path3
Path20 = os.path.join(Path1, Path2, Path3)
Path30 = os.path.join(Path2, Path1, Path3)
print('Path10 = ',Path10)
print('Path20 = ',Path20)
print('Path30 = ',Path30)