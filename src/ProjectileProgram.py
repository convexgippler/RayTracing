from dataclasses import dataclass
from tuple import *


@dataclass
class Projectile:
    position: Tuple
    velocity: Tuple


@dataclass
class Environment:
    gravity: Tuple
    wind: Tuple


def tick(environment: Environment, projectile: Projectile) -> Projectile:
    position = projectile.position + projectile.velocity
    velocity = projectile.velocity + environment.gravity + environment.wind
    return Projectile(position, velocity)


if __name__ == '__main__':
    p = Projectile(point(0, 1, 0), vector(0, 100, 0))
    e = Environment(vector(0, -0.1, 0), vector(-0.01, 0, 0))
    while p.position.y > 0:
        p = tick(e, p)
        print(f"position: {p.position}, velocity: {p.velocity}")
