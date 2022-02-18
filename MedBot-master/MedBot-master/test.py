# var point = this.items[i].questionPoints[this.questions[0].index];
# if (point) {
#     var up = ((2 * point.max - 1) * ans / 100 + 1 - point.max) * this.items[i].points;
#     var down = ((2 * point.max - 1) * ans / 100 + 1 - point.max) * this.items[i].points + ((2 * point.min - 1) * ans / 100 + 1 - point.min) * (1 - this.items[i].points);
#     this.items[i].points = down != 0 ? up / down : this.items[i].points;
# }

#  0.02      3 1.0 0.01 
 
ans=75
pmax=1.0
pmin = 0.01
vv=0.02
up = up = ((2 * pmax - 1) * ans / 100 + 1 - pmax) * vv;
down = ((2 * pmax - 1) * ans / 100 + 1 - pmax) * vv + ((2 * pmin - 1) * ans / 100 + 1 - pmin) * (1 - vv)
print(down)
print(up)

if down!=0:
    vv=up/down
print(vv)
# nvv = down != 0 ? up / down : this.items[i].points;