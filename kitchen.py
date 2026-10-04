
import sqlite3

class kitchen:
        def printorders(self):
            con = sqlite3.connect("rest.db")
            cur = con.cursor()
            orders=cur.execute("select * from orders").fetchall()
            print("\n--- order_list ---")
            for k in orders:
                print(f"{k[0]}: {k[1]}")
            print("-----------------\n")



        def delete_prepared_order(self,done_order,n):
            con = sqlite3.connect("rest.db")
            cur = con.cursor()
            cur.execute("delete from orders where type='{}' and table_num='{}'".format(done_order.strip().lower(),n))
            con.commit()

        def main(self):
            self.printorders()
            while True:
                prepare = input("any prepared order?(yes/no)")
                if prepare=="yes".lower().strip():
                    done_order=input("which one?")
                    n=input("table number")
                    self.delete_prepared_order(done_order, n)
                    self.printorders()
                elif prepare=="no".lower().strip():
                    print("ok\n")
                else:
                    print("wrong input, please try again.\n")
if __name__ == "__main__":
    k = kitchen()
    k.main()
