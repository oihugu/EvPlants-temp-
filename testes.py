import aplication

l_system = aplication.l_systems.L_system('F', {'F': {'r':'F+F--F+F'}})
l_system.save_animation('snowflake', 2, background='#CBC3E3')
