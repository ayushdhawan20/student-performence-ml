import pickle

model = pickle.load(open("model.pkl", "rb"))

attendance = int(input("Enter Attendance (%): "))
study_hours = float(input("Enter Study Hours: "))
marks = int(input("Enter Marks: "))

prediction = model.predict(
    [[attendance, study_hours, marks]]
)

print("\nPrediction:", prediction[0])