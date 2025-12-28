def show_menu() -> None:
    print("\n====== 📱 Contact Book v2.2 ======")
    print("1. + Yangi kontakt qoshish")
    print("2. 📄 Barcha kontaktlarni korish")
    print("3. 🔍 Kontaktni ism boyicha qidirish")
    print("4. 📧 Faqat @gmail.com kontaktlarni korish")
    print("5. 🚪 Dasturni yakunlash")


def is_valid_contact(contacts: list) -> any:
    
    if not contacts[0].isalpha():
        return "bu ism emas"
    
    elif len(contacts[1]) != 12:
        return "998991234456 shu ko'rinishda kiriting raqamni," 
    
    elif "@" in contacts[2] and len(contacts[2]) < 5:
        return "email uzubligi 5 tadan ko'p bo'lishligi kerak va emailda @ bo'lishligi kerak"
    
    else:
        return "ok"
    

def add_contact(contact_list: list[list]) -> None:
    name = input('Name: ').strip().title()
    phone = input('Phone: ').strip()
    email = input('Email: ').strip()

    contact = [name, phone, email]
    
    result = is_valid_contact(contact)
    if result == "ok":
        contact_list.append(contact)
        print('contact muvvaffaqiyatli qoshildi')
    else:
        print(f'contact xato . Sabab {result}')


def list_contacts(contact_list: list[list]) -> None:
    for contact in contact_list:
        print(contact)


def search_contact(contact_list: list[list]) -> None:
    search = input("Search: ").strip()

    for contact in contact_list:
        if search.lower() == contact[0].lower():
            print(contact, "1")
        
        elif search.lower() in contact[0].lower():
            print(contact, "2")
        
        else:
            print("Bunday ism mavjud emas")
        
        


def filter_gmail_contacts(contact_list: list[list]) -> None:
    for contact in contact_list:
        if contact[2].endswith('@gmail.com'):
            print(contact)


def main() -> None:
    contacts: list[list] = [
        ['Ali', '99123123123', 'ali@gmail.com'],
        ['Vali', '881231231231', 'vali@yandex.ru']
    ]

    while True:
        show_menu()
        choice = input("Tanlov (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            list_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            filter_gmail_contacts(contacts)
        elif choice == "5":
            print("👋 Dasturni yakunlayapmiz. Xayr!")
            break
        else:
            print("Notogri tanlov. Iltimos, 1 dan 5 gacha son kiriting.")

main()