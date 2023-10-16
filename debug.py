# from ants import *
# beehive, layout = Hive(AssaultPlan()), dry_layout
# dimensions = (1, 9)
# gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
# #
# # Testing ShortThrower miss
# ant = ShortThrower()
# out_of_range = Bee(2)
# gamestate.places["tunnel_0_0"].add_insect(ant)
# gamestate.places["tunnel_0_4"].add_insect(out_of_range)
# ant.action(gamestate)
# print(f'out_of_range.health: {out_of_range.health}\nexpected 2')



from ants import *
beehive, layout = Hive(AssaultPlan()), dry_layout
dimensions = (1, 9)
gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
#
# Testing fire does damage to all Bees in its Place
place = gamestate.places['tunnel_0_4']
fire = FireAnt(health=1)
place.add_insect(fire)        # Add a FireAnt with 1 health
place.add_insect(Bee(3))      # Add a Bee with 3 health
place.add_insect(Bee(5))      # Add a Bee with 5 health
place.bees[0].action(gamestate)  # The first Bee attacks FireAnt