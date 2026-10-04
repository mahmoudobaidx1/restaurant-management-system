import sqlite3

class costumer:
    def db(self):
        con = sqlite3.connect("rest.db")
        cur = con.cursor()
        menu = cur.execute("select * from menu").fetchall()
        return menu

    def print_menu(self):
        r= self.db()
        print("\n--- MENU ---")
        for k in r:
            print(f"{k[0]}: {k[1]}")
        print("------------\n")

    def get_order_details(self):
        r = self.db()

        while True:
            self.print_menu()
            ord = input("what would you like to order? ")

            for i in r:
                type = i[0]
                price=i[1]
                if ord.strip().lower() == type.lower():
                    print("the cost is: ")
                    print(price)
                    return type

            print("wrong input, please try again.\n")

    def t_num(self):
        table_num = input("enter table number: ")
        return table_num
    def addorder(self):
        type_val=self.get_order_details()
        table_number=self.t_num()
        con = sqlite3.connect("rest.db")
        cur = con.cursor()
        cur.execute("insert into orders (type,table_num) values('{}','{}')".format(type_val.strip().lower(),table_number))
        con.commit()

while True:

    if __name__ == "__main__":
        j=costumer()
        j.addorder()