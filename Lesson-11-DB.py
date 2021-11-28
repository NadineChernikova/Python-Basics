import psycopg2

conn = psycopg2.connect(dbname="***",
                        user="***",
                        password="***",
                        host="***",
                        port="***")

cursor = conn.cursor()

if conn:
    print("CONNECTION ================= ")

    select_query = "select * from public.salary;"
    execute_q = cursor.execute(select_query)

    get_query_result = cursor.fetchall()

    print("execute_q =", get_query_result)

    for i in get_query_result:
        print("id = ", i[0], "salary = ", i[1])

for i in range(0, 10):
    if conn:
        print("CONNECTION INSERT ======= ")

        salary = str(5000 + i*100)

        insert_query = "insert into public.salary(monthly_salary)" \
                                    "values (" + salary + ")"

        cursor.execute(insert_query)

        conn.commit()

cursor.close()


for i in range(0, 10):
    if conn:
        role_name = "'Python_" + str(i) + "'"

        insert_query = "insert into public.roles(role_title)" \
                                    "values (" + role_name + ")"

        print("insert_query", insert_query)

        cursor.execute(insert_query)

        conn.commit()

cursor.close()
