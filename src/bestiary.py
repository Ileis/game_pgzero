Monster = tuple[str, int, float, int, int, int, int]
# image, damage, speed, hp, speed_attack, projectile_speed, threshold

bestiary: dict[int, Monster] = {
    20: ('enemy_01', 3, 0.5, 10, 3, 5, 200),
    30: ('enemy_02', 5, 1, 10, 3, 250),
    36: ('enemy_03', 8, 0.3, 3, 60, 300),
    40: ('enemy_04', 10, 0.2, 3, 60, 400),
}