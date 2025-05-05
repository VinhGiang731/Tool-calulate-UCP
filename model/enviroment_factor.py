# UAW
class ecf_factor:
    def __init__(self):
        self.factors = [
                "Quen thuộc với dự án",
                "Kinh nghiệm ứng dụng",
                "Kinh nghiệm hướng đối tượng",
                "Năng lực lead phân tích",
                "Động lực",
                "Ổn định yêu cầu",
                "Nhân viên bán thời gian",
                "Độ khó ngôn ngữ lập trình"
            ]
        self.weights = [1.5, 0.5, 1, 0.5, 1, 2, -1, -1]

    def factors(self):
        return self.factors

    def weights(self):
        return self.weights
