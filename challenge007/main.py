def main():
    package = 'a(bc(def)g)h'
    c1 = 'a(bc(def)g)h'
    c2 = 'a(cb)de'
    c3 = 'abc(def(gh)i)jk'
    c4 = 'a(b(c))e'
    print(fix_packages(c3))

def fix_packages(packages):
    result = packages
    open_post = result.find('(')
    if open_post != -1:
        result = result[:open_post] + fix_packages(result[open_post+1:])
    close_post = result.find(')')
    if close_post != -1:
        result = result[:close_post][::-1] + result[close_post+1:]
    return result

""" No recursivo 
def fix_packages(packages):
    while '(' in packages:
        open_post = packages.rfind('(')  # Buscar el paréntesis más interno
        close_post = packages.find(')', open_post)  # Encontrar su cierre correspondiente
        # Invertir el contenido dentro de estos paréntesis
        inner = packages[open_post + 1:close_post][::-1]
        # Reemplazar la sección completa en la cadena
        packages = packages[:open_post] + inner + packages[close_post + 1:]
    return packages
"""


if __name__ == '__main__':
    main()



