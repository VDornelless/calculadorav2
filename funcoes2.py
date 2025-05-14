'''
Microatividade 6: Descrever a utilização
argumentos de funções no Python
'''

def loginUsuario(perfil):
    perfil = perfil.lower()
    if perfil == "admin":
        print("Bem-vindo, Administrador")
    else:
        print("Bem-vindo, Usuário")
    
print(loginUsuario("Admin"))