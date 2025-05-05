# UAW
class tcf_factor:
    def __init__(self):
        self.factors = [
            "Hệ thống phân tán",
            "Mục tiêu thời gian phản hồi/hiệu suất",
            "Hiệu quả của người dùng cuối",
            "Độ phức tạp xử lý nội bộ",
            "Khả năng tái sử dụng mã",
            "Dễ dàng cài đặt",
            "Dễ sử dụng",
            "Khả năng di chuyển sang các nền tảng khác",
            "Bảo trì hệ thống",
            "Xử lý đồng thời/song song",
            "Tính năng bảo mật",
            "Quyền truy cập cho bên thứ ba",
            "Đào tạo người dùng cuối"
        ]
        self.weights = [2.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0]

    def factors(self):
        return self.factors

    def weights(self):
        return self.weights