import tkinter as tk
from tkinter import ttk
from controller import UCPCalculator as c_ucp
from tkinter import messagebox as mg

from model import technical_factor as tcfs
from model import enviroment_factor as ecfs

import json


class UCPCalView:
    def __init__(self, root):
        self.tcf = tcfs.tcf_factor()
        self.ecf = ecfs.ecf_factor()
        width = 1500
        height = 700

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        self.height_layout = screen_height / 4

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.bg_color = "#f0f4f8"
        self.init_variables()

        self.root = root
        self.root.bind("<Key>", self.event_key)
        self.root.configure(bg=self.bg_color)

        self.root.geometry(f"{width}x{height}+{x}+{y - 30}")  # Điều chỉnh kích thước cửa sổ
        # self.root.geometry(f"{screen_width}x{screen_height}")
        # self.root.resizable(width=False, height=False)
        self.root.state('zoomed')
        self.root.title("Calculator UCP")

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        self.frame_actor = tk.LabelFrame(self.root, text="Actor", font=("Arial", 10, "bold"), fg="black", bg="white",
                                         height=self.height_layout)
        self.frame_use = tk.LabelFrame(self.root, text="Use case", font=("Arial", 10, "bold"), fg="black", bg="white",
                                       height=self.height_layout)

        self.frame_tcf = tk.LabelFrame(self.root, text="Technical Complexity Factor (TCF)", font=("Arial", 10, "bold"),
                                       fg="black", bg="white",
                                       height=self.height_layout)

        self.frame_ecf = tk.LabelFrame(self.root, text="Environmental Complexity Factor (ECF)",
                                       font=("Arial", 10, "bold"), fg="black", bg="white",
                                       height=self.height_layout)

        self.frame_output = tk.LabelFrame(self.root, bg=self.bg_color, text="Output", font=("Arial", 10, "bold"))

        self.frame_report = tk.LabelFrame(self.root, bg=self.bg_color, text="Report", font=("Arial", 10, "bold"))

        self.frame_actor.grid(row=0, column=0, sticky="nsew", padx=(20, 0))
        self.frame_use.grid(row=0, column=1, sticky="nsew", padx=(0, 20))
        self.frame_tcf.grid(row=2, column=0, sticky="nsew", padx=(20, 0))
        self.frame_ecf.grid(row=2, column=1, sticky="nsew", padx=(0, 20))
        self.frame_output.grid(row=4, column=0, sticky="nsew", padx=(10, 0))
        self.frame_report.grid(row=4, column=1, sticky="nsew", padx=(0, 10))

        # factor
        self.technical_factors = self.factor_frame(self.frame_tcf,
                                                   self.tcf.factors,
                                                   self.tcf.weights)

        self.environmental_factor = self.factor_frame(self.frame_ecf,
                                                      self.ecf.factors,
                                                      self.ecf.weights)

        # lable
        # self.label(self.frame_actor, "Factors")
        # self.label(self.frame_use, "PE")
        self.label(self.frame_use, "Effort Actual")
        self.label(self.frame_actor, "Hours/UCP")

        # entry
        self.entry_actor(self.frame_actor)
        self.entry_use(self.frame_use)

        # btn
        self.btn_ucp()

        # result
        self.lbl_result = tk.Label(self.frame_output, text="Empty", font=("Arial", 12), bg=self.bg_color,
                                   anchor="nw", justify="center")
        self.lbl_result.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # report
        self.lbl_report = tk.Label(self.frame_report, text="Empty", font=("Arial", 12), bg=self.bg_color,
                                   anchor="nw", justify="center")
        self.lbl_report.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


        self.entry_actor_s.focus_set()



    def init_variables(self):
        self.txt_as = tk.StringVar()
        self.txt_aa = tk.StringVar()
        self.txt_ac = tk.StringVar()

        self.txt_us = tk.StringVar()
        self.txt_ua = tk.StringVar()
        self.txt_uc = tk.StringVar()

        self.txt_f = tk.StringVar()
        self.txt_pe = tk.StringVar()
        self.txt_eofucp = tk.StringVar()
        self.txt_effort_acturl = tk.StringVar()

    def label(self, frame, addition=""):
        view = tk.Frame(frame, bg="#3498db", height=2, width=700)
        view.place(x=15, y=5)

        lbl_simple = tk.Label(frame, text="Simple", font=("Arial", 11), bg="white", width=7, anchor="w")
        lbl_simple.place(x=20, y=25)

        lbl_simple = tk.Label(frame, text="Average", font=("Arial", 11), bg="white", width=7, anchor="w")
        lbl_simple.place(x=20, y=65)

        lbl_simple = tk.Label(frame, text="Complex", font=("Arial", 11), bg="white", width=7, anchor="w")
        lbl_simple.place(x=20, y=105)

        lbl_simple = tk.Label(frame, text=addition, font=("Arial", 11), bg="white", width=10, anchor="w")
        lbl_simple.place(x=20, y=145)

    def entry_actor(self, frame):
        self.entry_actor_s = tk.Entry(frame, font=("Arial", 12), width=15, bg="#f1f1f1", textvariable=self.txt_as)
        self.entry_actor_s.place(x=110, y=25)

        self.entry_actor_a = tk.Entry(frame, font=("Arial", 12), width=15, bg="#f1f1f1", textvariable=self.txt_aa)
        self.entry_actor_a.place(x=110, y=65)

        self.entry_actor_c = tk.Entry(frame, font=("Arial", 12), width=15, bg="#f1f1f1", textvariable=self.txt_ac)
        self.entry_actor_c.place(x=110, y=105)

        self.entry_actor_f = tk.Entry(frame, font=("Arial", 12), width=15, bg="#f1f1f1", textvariable=self.txt_eofucp)
        self.entry_actor_f.place(x=110, y=145)

    def entry_use(self, frame):
        self.entry_user_s = tk.Entry(frame, font=("Arial", 12), width=15, bg="#f1f1f1", textvariable=self.txt_us)
        self.entry_user_s.place(x=110, y=25)

        self.entry_user_a = tk.Entry(frame, font=("Arial", 12), width=15, bg="#f1f1f1", textvariable=self.txt_ua)
        self.entry_user_a.place(x=110, y=65)

        self.entry_user_c = tk.Entry(frame, font=("Arial", 12), width=15, bg="#f1f1f1", textvariable=self.txt_uc)
        self.entry_user_c.place(x=110, y=105)

        # self.entry_user_pe = tk.Entry(frame, font=("Arial", 12), width=15, bg="#f1f1f1", textvariable=self.txt_pe)
        # self.entry_user_pe.place(x=100, y=145)

        self.entry_user_pe = tk.Entry(frame, font=("Arial", 12), width=15, bg="#f1f1f1",
                                      textvariable=self.txt_effort_acturl)
        self.entry_user_pe.place(x=110, y=145)

    def factor_frame(self, frame, factors, weights):
        canvas = tk.Canvas(frame, bg="white", height=self.height_layout)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="white")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Lưu trữ các yếu tố
        scrollable_frame.factors = []

        for i, (factor, weight) in enumerate(zip(factors, weights)):
            row_frame = tk.Frame(scrollable_frame, bg="white")
            row_frame.pack(fill="x", padx=5, pady=2)

            # yếu tố
            label = tk.Label(row_frame, text=factor, font=("arial", 10), width=30, anchor='w', bg="white")
            label.pack(side=tk.LEFT, padx=5)

            # Trọng số
            weight_label = tk.Label(row_frame, text=f"(Trọng số: {weight})", width=15, bg="white")
            weight_label.pack(side=tk.LEFT, padx=5)

            # Ô input
            value_var = tk.StringVar(value='0')
            value_entry = tk.Entry(row_frame, textvariable=value_var, width=10, bg="white")
            value_entry.pack(side=tk.LEFT, padx=5)

            # Lưu yếu tố
            scrollable_frame.factors.append({
                'name': factor,
                'weight': weight,
                'value_var': value_var
            })

        return scrollable_frame

    def create_scrollable_output_report(self, parent_frame):
        canvas = tk.Canvas(parent_frame, bg=self.bg_color, highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.bg_color)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        return scrollable_frame

    def btn_ucp(self):
        btn_ucp = tk.Button(self.root, text="Calculate UCP", font=("Arial", 12), width=200, bg="#38b0ff", fg="white",
                            command=self.calculator_ucp)
        btn_ucp.grid(row=3, column=0, padx=20, pady=10)

        btn_clear = tk.Button(self.root, text="Clear", font=("Arial", 12), width=200, bg="#38b0ff", fg="white",
                              command=self.clear)
        btn_clear.grid(row=3, column=1, padx=20)

    def calculator_ucp(self):
        # entries = [self.txt_as.get(), self.txt_aa.get(), self.txt_ac.get(), self.txt_us.get(), self.txt_ua.get(),
        #            self.txt_uc.get(), self.txt_f.get(), self.txt_pe.get()]

        entries = [self.txt_as.get(), self.txt_aa.get(), self.txt_ac.get(), self.txt_us.get(), self.txt_ua.get(),
                   self.txt_uc.get(), self.txt_eofucp.get(), self.txt_effort_acturl.get()]

        flag = True
        for value in entries:
            if not self.is_valid_number(value):
                flag = False

        print(flag)

        flag2 = self.is_valid_number_factor(self.technical_factors) and self.is_valid_number_factor(
            self.environmental_factor)

        if not flag or not flag2:
            self.lbl_result.configure(text="Input must be number and !empty", fg="red")
        else:
            # cal_ucp = c_ucp.UCPCalculator(int(self.txt_as.get()), int(self.txt_aa.get()), int(self.txt_ac.get()),
            #                               int(self.txt_us.get()),
            #                               int(self.txt_ua.get()),
            #                               int(self.txt_uc.get()), int(self.txt_f.get()), int(self.txt_pe.get()),
            #                               self.technicalC_factors,
            #                               self.environmental_factor)

            cal_ucp = c_ucp.UCPCalculator(int(self.txt_as.get()), int(self.txt_aa.get()), int(self.txt_ac.get()),
                                          int(self.txt_us.get()),
                                          int(self.txt_ua.get()),
                                          int(self.txt_uc.get()),
                                          int(self.txt_eofucp.get()),
                                          self.technical_factors,
                                          self.environmental_factor,
                                          self.txt_effort_acturl.get())

            # uaw = cal_ucp.cal_uaw()
            # uucw = cal_ucp.cal_uucw()
            # uucp = cal_ucp.cal_uucp()
            # ucp = cal_ucp.cal_ucp()
            # effort = cal_ucp.cal_effort()
            print(self.txt_eofucp.get())

            json_result = cal_ucp.cal_ucp()

            data = json.loads(json_result)

            report = data['report']
            data_report = json.loads(report)

            self.lbl_result.configure(text=data['result'],
                                      fg=data['color'],
                                      justify="left",
                                      anchor="nw")

            self.lbl_report.configure(text=f"{data_report['result']} {data_report['feedback']}",
                                      fg=data['color'],
                                      justify="left",
                                      anchor="nw")

    def clear(self):
        self.txt_as.set('')
        # focus txt_as
        self.entry_actor_s.focus_set()
        self.txt_aa.set('')
        self.txt_ac.set('')

        self.txt_us.set('')
        self.txt_ua.set('')
        self.txt_uc.set('')

        self.txt_f.set('')
        self.txt_pe.set('')
        self.txt_effort_acturl.set('')
        self.txt_eofucp.set('')

        for factor in self.technical_factors.factors:
            factor['value_var'].set('0')

        # Reset environmental factors về 0 (nếu muốn)
        for factor in self.environmental_factor.factors:
            factor['value_var'].set('0')

        self.lbl_result.configure(text="Empty", fg="black")
        self.lbl_report.configure(text="Empty", fg="black")

    def is_valid_number(self, value):
        if not value.strip():
            return False

        try:
            float(value)
            return True
        except ValueError:
            return False

    def is_valid_number_factor(self, factors_group):
        for factor in factors_group.factors:
            value = factor['value_var'].get()
            if not value.strip():
                return False

            try:
                int(value)
            except ValueError:
                return False
        return True

    def event_key(self, event):
        if event.keysym == "Escape":
            rs = mg.askyesno("Confirm", "Do you wanna exit?")
            if rs:
                self.root.destroy()

        elif event.keysym == "Return":
            self.calculator_ucp()


if __name__ == "__main__":
    root = tk.Tk()
    app = UCPCalView(root)
    root.mainloop()
