from flask import Flask, jsonify, request
app=Flask(__name__)
@app.route('/', methods=(['POST', 'GET']))
def index():
	if (request.method=='POST'):
		some_json=request.get_json()
		return jsonify({"You Sent":some_json}), 201
	else:
		return jsonify({"Error":"Lost Error"})
@app.route('/bmi/<int:weight>/<float:height>', methods=['GET'])
def get_bmi(weight,height):
	bmi=int(weight/(height*height))
	if(bmi in range(18,24)):
		msg="Your BMI falls in Healthy Category"

	if(bmi in range(18)):
		msg="Your BMI falls in UNDERWEIGHT Category"
	if(bmi in range(24,50)):
		msg="Your BMI falls in OVERWEIGHT Category"

	return jsonify({"Weight":weight,"height":height,"BMI: ":bmi,"Advice":msg})

if __name__ == '__main__':
	app.run(debug=True)