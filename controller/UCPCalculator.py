from model import Actor as at
from model import UseCase as us
import json


class UCPCalculator:

    def __init__(self, txt_as=0, txt_aa=0, txt_ac=0, txt_us=0, txt_ua=0, txt_uc=0, txt_f=0, txt_pe=0, tcf_factors=[],
                 ecf_factors=[]):
        self.txt_as = txt_as
        self.txt_aa = txt_aa
        self.txt_ac = txt_ac

        self.txt_us = txt_us
        self.txt_ua = txt_ua
        self.txt_uc = txt_uc

        self.txt_f = txt_f
        self.txt_pe = txt_pe

        self.tcf_factors = tcf_factors
        self.ecf_factors = ecf_factors

        self.uaw = 0.0
        self.uucw = 0.0
        self.uucp = 0.0
        self.vaf = 0.0
        self.ucp = 0.0
        self.effort = 0.0

        self.actor = at.Actor(txt_as, txt_aa, txt_ac)
        self.userCase = us.UseCase(txt_us, txt_ua, txt_uc)

        # self.actor = at.Actor(6, 0, 0)
        # self.userCase = us.UseCase(1, 2, 2)

    def __init__(self, txt_as=0, txt_aa=0, txt_ac=0, txt_us=0, txt_ua=0, txt_uc=0, txt_effort_ofHours=0, tcf_factors=[],
                 ecf_factors=[], effort_actual=0):
        self.txt_as = txt_as
        self.txt_aa = txt_aa
        self.txt_ac = txt_ac

        self.txt_us = txt_us
        self.txt_ua = txt_ua
        self.txt_uc = txt_uc
        self.txt_effort_ofHours = txt_effort_ofHours
        self.effort_actual = effort_actual

        self.tcf_factors = tcf_factors
        self.ecf_factors = ecf_factors

        self.uaw = 0.0
        self.uucw = 0.0
        self.uucp = 0.0
        self.vaf = 0.0
        self.ucp = 0.0
        self.effort = 0.0

        self.actor = at.Actor(txt_as, txt_aa, txt_ac)
        self.userCase = us.UseCase(txt_us, txt_ua, txt_uc)

        # self.actor = at.Actor(6, 0, 0)
        # self.userCase = us.UseCase(1, 2, 2)

    def cal_uaw(self):
        try:
            self.uaw = self.actor.calculate_UAW()
            return self.uaw
        except ValueError:
            return 0

    def cal_uucw(self):
        try:
            self.uucw = self.userCase.calculate_UUCW()
            return self.uucw
        except ValueError:
            return 0

    def cal_uucp(self):
        try:
            self.uucp = self.uaw + self.uucw
            return self.uucp
        except ValueError:
            return 0

    def cal_vaf(self):
        try:
            self.vaf = float(0.65 + 0.01 * self.txt_f)
            return self.vaf
        except ValueError:
            return 0

    def cal_tcf(self):
        self.tcf_factors_value = 0.0
        try:
            self.tcf_total = sum(
                factor['weight'] * int(factor['value_var'].get())
                for factor in self.tcf_factors.factors
            )

            self.tcf_factors_value = 0.6 + (self.tcf_total * 0.01)
            return self.tcf_factors_value
        except ValueError:
            return self.tcf_factors_value

    def cal_ecf(self):
        self.ecf_factors_value = 0.0
        try:
            self.ecf_total = sum(
                factor['weight'] * int(factor['value_var'].get())
                for factor in self.ecf_factors.factors
            )

            self.ecf_factors_value = 1.4 + (-0.03 * self.ecf_total)
            return self.ecf_factors_value
        except ValueError:
            return self.ecf_factors_value

    def cal_ucp(self):
        try:
            self.cal_uaw()
            self.cal_uucw()
            # self.cal_uucp()
            # self.cal_vaf()
            self.cal_tcf()
            self.cal_ecf()
            print(f"UUCW: {self.uucw}")
            print(f"uaw: {self.uaw}")
            print(f"tcf_factors_value: {self.tcf_factors_value}")
            print(f"ecf_factors_value: {self.ecf_factors_value}")
            ucp = float((self.uucw + self.uaw) * self.tcf_factors_value * self.ecf_factors_value)
            effort = float(ucp * self.txt_effort_ofHours)
            print(f"ucp: {ucp}")
            print(f"effort: {effort}")

            return json.dumps({
                "result": f"""Kết Quả Ước Lượng Use Case Points:
------------------------------------------------------
Unadjusted Actor Weight (UAW): {self.uaw:.2f}
Unadjusted Use Case Weight (UUCW): {self.uucw:.2f}
Technical Complexity Factor (TCF): {self.tcf_factors_value:.2f}
Environmental Complexity Factor (ECF): {self.ecf_factors_value:.2f}
Use Case Points(UCP): {ucp:.2f}
Estimated  Effort (Hours): {effort:.2f}
                        """,
                "report": f"{self.report_effort(effort)}",
                "color": "black"
            })

        except ValueError:
            return json.dumps({
                "result": "Có lỗi trong quá trình tính toán!!!",
                "color": "red"
            })

    def report_effort(self, effort_predicted):
        effort_actual = int(self.effort_actual)

        # sự khác biệt và tỉ lệ chênh lệch
        diff = effort_actual - effort_predicted

        if effort_actual != 0:
            percent_diff = (diff / effort_predicted) * 100
        else:
            percent_diff = 0

        accuracy = 100 - abs(percent_diff)

        # nhận xét
        result = f"""Báo cáo dự đoán effort và so sánh thực tế:
---------------------------------------------------------------
Effort predicted: {effort_predicted:.2f}
Effort actual: {effort_actual:.2f}
Effort diff: {diff:.2f}
Percent diff: {percent_diff:.2f}%
Accuracy: {accuracy:.2f}"""

        level, comment = self.feedback_percent_diff(percent_diff)
        rating = self.feedback_accuracy(accuracy)

        feedback = f"\nMức độ chênh lệch:\n- {level} - {comment}\nMức độ chính xác:\n- {rating}"

        print(result)
        print(feedback)

        return json.dumps({
            "result": result,
            "feedback": feedback
        })

    def feedback_percent_diff(self, percent_diff):
        if 0 <= percent_diff <= 10:
            level = "Rất nhỏ (chính xác cao)"
            comment = "Mô hình dự đoán rất tốt"
        elif 10 < percent_diff <= 20:
            level = "Nhỏ"
            comment = "Chấp nhận được"
        elif 20 < percent_diff <= 30:
            level = "Vừa phải"
            comment = "Cần xem xét mô hình"
        elif percent_diff > 30:
            level = "Lớn"
            comment = "Sai lệch nhiều, mô hình cần cải thiện"
        else:
            level = "Không hợp lệ"
            comment = "Giá trị không hợp lệ"

        return level, comment

    def feedback_accuracy(self, accuracy):
        if accuracy >= 90:
            rating = "Rất chính xác"
        elif 80 <= accuracy < 90:
            rating = "Chính xác"
        elif 70 <= accuracy < 80:
            rating = "Chấp nhận được"
        elif accuracy < 70:
            rating = "Thấp, cần cải tiến"
        else:
            rating = "Giá trị không hợp lệ"
        return rating

    def cal_effort(self):
        try:
            self.effort = self.ucp * self.txt_pe
            return self.effort
        except ValueError:
            return 0

# if __name__ == "__main__":
#     calculator = UCPCalculator()
#     print(calculator.cal_uaw())
#     print(calculator.cal_uucw())
#     print(calculator.cal_uucp())
#     print(calculator.cal_ucp())
#     print(calculator.cal_effort())
