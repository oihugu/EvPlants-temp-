from  Application.lSystems import L_system

sys = L_system('F', {'F': {'r' : 'F+F-F-F+F'}})
plt = sys.run(3)
plt.show()