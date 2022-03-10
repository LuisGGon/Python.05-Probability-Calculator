import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.args = dict(kwargs)
        balls = []
        for ball in self.args.keys():
            count = 0
            while count <self.args[ball]:
                balls.append(ball)
                count = count +1
        self.contents = balls

    def draw(self, num):
        draw = []
        if num>=len(self.contents):
            draw = self.contents.copy()
            self.contents.clear()
            return draw
        else:
            count = 0
            while count < num:
                rand = random.randrange(0, len(self.contents), 1)
                draw.append(self.contents.pop(rand))
                count = count +1
            return draw
            
              


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    count = 0
    expected_balls = ordered_balls(expected_balls)
    for k in range(0,num_experiments):
        new_hat = copy.deepcopy(hat)
        balls_drawn = new_hat.draw(num_balls_drawn)
        inner_count = 0
        for ball in expected_balls:
            if ball in balls_drawn:
                balls_drawn.pop(balls_drawn.index(ball))
                inner_count += 1

              
        if inner_count == len(expected_balls):
            count += 1
      
    return count/num_experiments

def ordered_balls(balls):
    ord_balls = []
    for ball in balls.keys():
            count = 0
            while count < balls[ball]:
                ord_balls.append(ball)
                count = count +1
    return sorted(ord_balls)
