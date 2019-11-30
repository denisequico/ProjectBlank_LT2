import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

products_db = myclient["products"]

order_management_db = myclient["order_management"]

branches_db = myclient["branches"]

stalls_db = myclient["stalls"]

def get_product(code):
    products_coll = products_db["products"]
    product = products_coll.find_one({"code":code})
    return product

def get_mana():
    product_list = []
    mana_coll = products_db["mana"]
    for p in mana_coll.find({}):
        product_list.append(p)

    return product_list

def get_djchick():
    product_list = []
    djchick_coll = products_db["djchick"]
    for p in djchick_coll.find({}):
        product_list.append(p)

    return product_list

def get_downtownfillet():
    product_list = []
    downtownfillet_coll = products_db["downtownfillet"]
    for p in downtownfillet_coll.find({}):
        product_list.append(p)
    
    return product_list

def get_branch(code):
    branches_coll = products_db["branches"]
    branches = branches_coll.find_one({"code":code})
    return branch

def get_branches():
    branch_list = []
    branches_coll = products_db["branches"]
    for p in branches_coll.find({}):
        branch_list.append(p)
    return branch_list

def get_stall(code):
    stalls_coll = stalls_db["stalls"]
    stall = stalls_coll.find_one({"code":code})
    return stall

def get_stalls():
    stall_list = []
    stalls_coll = stalls_db["stalls"]
    for p in stalls_coll.find({}):
        stall_list.append(p)
    return stall_list

def get_user(username):
    customers_coll = order_management_db['customers']
    user = customers_coll.find_one({"username":username})
    return user

def create_order(order):
    orders_coll = order_management_db['orders']
    orders_coll.insert(order)

def count_orders (username):
    orders_coll = order_management_db ['orders']
    numberoforders = []
    numberoforders = orders_coll.count ({"username": username} )
    return numberoforders

def get_orders(username):
    order_list = []
    orders_coll = order_management_db["orders"]

    for p in orders_coll.find({"username":username}):
        order_list.append(p)
    return order_list

def change_db(username,newpassword):
    password_coll = order_management_db["customers"]    
    customer = {"username":username}
    changepassword = {"$set":{"password":newpassword}}
    password_coll.find_one_and_update(customer,changepassword)
