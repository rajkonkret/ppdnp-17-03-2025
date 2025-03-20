# import fun1
import pakiet
from pakiet import fun
import pakiet.fun as pk  # jako alias

# fun1.dodaj()

# po dodaniu __all__
pakiet.powitanie()
# AttributeError: module 'pakiet' has no attribute 'info'
# pakiet.info()

# from pakiet import fun
fun.info()
fun.powitanie()

# import pakiet.fun as pk
pk.info()
pk.powitanie()
# pakiet.fun
# Cześć
# Jestem pakietem
# Cześć
# Jestem pakietem
# Cześć
