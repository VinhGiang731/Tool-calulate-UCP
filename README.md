Use Case Points (UCP) Calculator

Introduction
The Use Case Points (UCP) Calculator is a tool designed to estimate software development effort based on the Use Case Points method.
It helps project managers assess project complexity in detail and make more accurate predictions about the required time and resources.

Key Features
Manage a list of actors and evaluate their complexity

Manage a list of use cases with transaction count details

Customize Technical Complexity Factors (TCF)

Customize Environmental Factors (EF)

Automatically calculate UAW, UUCW, TCF, and ECF

Estimate the expected effort (man-hours)

User Guide
1. Manage Actors
Each actor in the system is evaluated based on the complexity of its interaction:

![image](https://github.com/user-attachments/assets/ca4b51c3-a0a7-4398-ae54-58e4a0b142b2)

How to add an actor: Enter the number of actors by weight.

2. Manage Use Cases
Each use case is evaluated based on:
- General complexity
- Number of transactions

How to add a use case: Enter the number of use cases by weight.

Use case points are based on:

![image](https://github.com/user-attachments/assets/7ca97ee5-ad27-4ba3-981e-3aecaf16a503)

3. Adjust Technical Complexity Factors (TCF)
This section includes 13 technical factors, each rated on a scale from 0–5:

![image](https://github.com/user-attachments/assets/1b815351-78b6-4b43-bb6f-ec921c59d20f)

How to adjust:
(1). Evaluate each factor on a scale from 0–5
  0: Not relevant/no impact
  3: Medium impact
  5: Strong impact

(2). Enter the value in the corresponding field

4. Adjust Environmental Factors (EF)
This section includes 8 environmental factors, each rated on a scale from 0–5:

![image](https://github.com/user-attachments/assets/86cd00a2-70e2-49b8-9b2b-8bf1b1f6b64a)

How to adjust:

(1).Evaluate each factor on a scale from 0–5
  0: Not relevant/no impact
  3: Medium impact
  5: Strong impact
(2).Enter the value in the corresponding field

5. Calculate UCP
After entering all required information, click the "Calculate UCP" button.
The system will display results including:
Unadjusted Actor Weight (UAW): Total actor points
Unadjusted Use Case Weight (UUCW): Total use case points
Technical Complexity Factor (TCF)
Environmental Complexity Factor (ECF)
Use Case Points (UCP): Final UCP value
Estimated Effort (hours): UCP × 20
Understanding the Calculation Formula

UAW: Total score of all actors
UUCW: Total score of all use cases
TCF = 0.6 + (0.01 × Total Technical Factor score)
ECF = 1.4 + (-0.03 × Total Environmental Factor score)
UCP = (UAW + UUCW) × TCF × ECF
Estimated Effort = UCP × 20 (man-hours)

Important Notes
The estimation results based on UCP should be used for reference only
The coefficient "20 hours per UCP" can be adjusted depending on organizational practice
It is recommended to combine UCP with other estimation methods for higher accuracy
Consult with domain experts to better assess technical and environmental factors
Contact for Support
If you need additional support or have feedback about the tool, please contact:

Email: dinhvinhgiang345@gmail.com
