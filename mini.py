orders = [
    {'id': 'HD01', 'name': 'Dai ly Hoang Long', 'price': 45000000, 'status': 'Paid'},
    {'id': 'HD02', 'name': 'Tap hoa Minh Thu', 'price': 15000000, 'status': 'Unpaid'}
]

def view_orders():
    print(f"{'Ma don':<10} | {'Ten dai ly':<20} | {'Gia tri':<10} | {'Trang thai':<10}")
    if not orders:
        print('Chua co don hang nao')
        return
    for o in orders:
        print(f"{o['id']:<10} | {o['name']:<20} | {o['price']:<10} | {o['status']:<10}")

def check_none(keyword):
    if keyword == '':
        return False
    return keyword

def validate_nums(num):
    try:
        num = int(num)
        return num
    except ValueError:
        return None

def add_order():
    print('--- TẠO MỚI ĐƠN HÀNG ---')
    while True:
        id = input('Nhập mã đơn hàng: ').strip()
        if not check_none(id):
            print('Mã đơn hàng không được để trống!')
            continue

        found = False
        for o in orders:
            if o['id'] == id:
                found = True
                break
        if found:
            print('[Lỗi]: Mã đơn hàng này đã tồn tại trong hệ thống! (ERR-01)')
            return
        break

    while True:
        name = input('Nhập tên đại lý: ').strip()
        if not check_none(name):
            print('Tên đại lý không được để trống!')
            continue
        break

    while True:
        price = input('Nhập giá trị đơn hàng (VND): ').strip()
        price = validate_nums(price)
        if price is None:
            print('Giá trị đơn hàng phải là số nguyên!')
            continue
        break

    orders.append({'id': id, 'name': name, 'price': price, 'status': 'Unpaid'})
    print(f'[Thành công]: Đơn hàng {id} đã được tạo thành công!')

def update_status():
    print('--- CẬP NHẬT TRẠNG THÁI THANH TOÁN ---')
    id = input('Nhập mã đơn hàng cần cập nhật: ').strip()

    index = -1
    for i, o in enumerate(orders):
        if o['id'] == id:
            index = i
            break

    if index == -1:
        print(f'[Lỗi]: Không tìm thấy đơn hàng nào có mã [{id}]! (ERR-03)')
        return

    if orders[index]['status'] == 'Paid':
        print('[Lỗi]: Đơn hàng này đã được thanh toán trước đó! (ERR-04)')
        return

    orders[index]['status'] = 'Paid'
    print(f"Tìm thấy đơn hàng của: {orders[index]['name']} (Giá trị: {orders[index]['price']})")
    print(f'[Thành công]: Đơn hàng {id} đã được cập nhật trạng thái ĐÃ THANH TOÁN!')

def calc_revenue():
    print('--- BÁO CÁO TÀI CHÍNH DOANH NGHIỆP ---')

    total = 0
    for o in orders:
        if o['status'] == 'Paid':
            total += o['price']

    if total >= 100000000:
        discount_rate = 5
    else:
        discount_rate = 0

    discount = total * discount_rate // 100

    print(f'+ Tổng doanh thu thực tế (Đã thanh toán): {total:,} VND')
    print(f'+ Tỷ lệ chiết khấu áp dụng: {discount_rate}%')
    print(f'+ Số tiền chiết khấu đại lý nhận lại: {discount:,} VND')

while True:
    print('\n--- QUẢN LÝ ĐƠN HÀNG ĐẠI LÝ ---')
    print('1. Xem danh sách đơn hàng')
    print('2. Tạo mới đơn hàng')
    print('3. Cập nhật trạng thái thanh toán')
    print('4. Báo cáo tài chính')
    print('5. Thoát')

    choice = input('Mời chọn chức năng (1-5): ').strip()

    match choice:
        case '1':
            view_orders()
        case '2':
            add_order()
        case '3':
            update_status()
        case '4':
            calc_revenue()
        case '5':
            print('Tạm biệt!')
            break
        case _:
            print('Chức năng không hợp lệ, vui lòng chọn lại (1-5)!')