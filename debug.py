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



# from ants import *
# beehive, layout = Hive(AssaultPlan()), dry_layout
# dimensions = (1, 9)
# gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
# #
# # Testing fire does damage to all Bees in its Place
# place = gamestate.places['tunnel_0_4']
# fire = FireAnt(health=1)
# place.add_insect(fire)        # Add a FireAnt with 1 health
# place.add_insect(Bee(3))      # Add a Bee with 3 health
# place.add_insect(Bee(5))      # Add a Bee with 5 health
# place.bees[0].action(gamestate)  # The first Bee attacks FireAnt


# from ants import *
# beehive, layout = Hive(AssaultPlan()), dry_layout
# dimensions = (1, 9)
# gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
# #
# # Testing HungryAnt eats and chews
# hungry = HungryAnt()
# bee1 = Bee(1000)              # A Bee with 1000 health
# place = gamestate.places["tunnel_0_0"]
# place.add_insect(hungry)
# place.add_insect(bee1)         # Add the Bee to the same place as HungryAnt
# hungry.action(gamestate)
# bee1.health

# bee2 = Bee(1)                 # A Bee with 1 health
# place.add_insect(bee2)
# for _ in range(3):
#     hungry.action(gamestate)     # Digesting...not eating



# from ants import *
# beehive, layout = Hive(AssaultPlan()), dry_layout
# dimensions = (1, 9)
# gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
# #
# # Testing HungryAnt only waits when chewing
# hungry = HungryAnt()
# place = gamestate.places["tunnel_0_0"]
# place.add_insect(hungry)
# # Wait a few turns before adding Bee
# for _ in range(5):
#     hungry.action(gamestate)  # shouldn't be chewing


# from ants import *
# beehive, layout = Hive(AssaultPlan()), dry_layout
# dimensions = (1, 9)
# gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
# #
# # Testing HungryAnt eats and chews
# hungry = HungryAnt()
# bee1 = Bee(1000)              # A Bee with 1000 health
# place = gamestate.places["tunnel_0_0"]
# place.add_insect(hungry)
# place.add_insect(bee1)         # Add the Bee to the same place as HungryAnt
# hungry.action(gamestate)
# bee1.health



from ants import *
beehive, layout = Hive(AssaultPlan()), dry_layout
gamestate = GameState(None, beehive, ant_types(), layout, (1, 9))
#
# Any Container Ant can be added after another ant
container = ContainerAnt()
other_ant = ThrowerAnt()
place = gamestate.places['tunnel_0_0']
place.add_insect(other_ant)  # Other ant in place first
place.ant is other_ant

place.add_insect(container)
place.ant is container