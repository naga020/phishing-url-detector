test_url = "http://example-login.com"
features = pd.DataFrame([extract_features(test_url)])
prediction = model.predict(features)[0]
print("Result:", "Phishing" if prediction == 1 else "Safe")
