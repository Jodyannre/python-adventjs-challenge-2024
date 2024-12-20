import re
from operator import contains


def main():
    agenda = "+34-600-123-456 Calle Gran Via 12 <Juan Perez>\n" \
            "Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654\n" \
            "<Carlos Ruiz> +1-800-555-0199 Fifth Ave New York\n"

    agende = "+34-600-123-456 Calle Gran Via 12 <Juan Perez>\n" \
            "Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654\n" \
            "<Carlos Ruiz> +1-800-555-0199 Fifth Ave New York"

    phone = '34-600-123-456'
    phone2 = '600-987'
    phone3 = '111'
    phone4 = '1'
    phone5 = "600-987"
    print(find_in_agenda(agenda,phone))
    print(find_in_agenda(agenda,phone2))
    print(find_in_agenda(agenda,phone3))
    print(find_in_agenda(agenda,phone4))
    print(find_in_agenda(agenda,phone5))






def find_in_agenda(agenda: str, phone: str) -> dict | None:
    telefono = r"(?:\+\d{1,2}-\d{3}-\d{3}-\d{3})"
    nombre = r"(?:[A-Za-z\s]+)"
    direccion = r"(?:[^\n<>+-]+)"
    line_start = r"(?:^|\s)"
    line_end = r"(?:\s|$)"
    phone_group = rf"(?P<phone>{telefono})"
    name_group = rf"<(?P<name>{nombre})>"
    address_group = rf"{line_start}(?P<address>{direccion}){line_end}"
    result = {}
    #Condición de salida temprana
    conteo = agenda.count(phone)
    if conteo == 0 or conteo > 1:
        return None
    conteo = 0

    for linea in agenda.splitlines():
        r_phone = re.search(phone_group, linea)
        r_name = re.search(name_group, linea)
        r_address = re.search(address_group, linea)

        if conteo > 1:
            return None

        if phone in r_phone["phone"]:
            conteo += 1
            result["name"] = r_name["name"]
            result["address"] = r_address["address"]

    if conteo == 0:
        return None

    return result



if __name__ == '__main__':
    main()