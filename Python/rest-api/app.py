from flask import Flask, jsonify, request
from flask.wrappers import Response
from flask_restplus import Api, fields, Resource
from coffeeModel import *
from setting import *

api = Api(
    app=app,
    version="1.0",
    title="Senjapedia",
    description="Manage coffee for senja lovers",
)

api = api.namespace("coffee", description="Senjapedia Coffee Operations")

# models
coffee_model = api.model(
    "Coffee Model",
    {
        "id": fields.Integer(description="id"),
        "name": fields.String(
            required="True",
            description="Name of the coffee bean",
            help="Name cannot be blank",
        ),
        "origin": fields.String(
            required="True",
            description="origin of the coffee bean",
            help="origin cannot be blank",
        ),
        # "usage": fields.List(
        #     fields.String,
        #     required="True",
        #     description="name of the method to make coffee",
        #     help="usage cannot be blank",
        # ),
        "usage": fields.String(
            required="True",
            description="name of the method to make coffee",
            help="usage cannot be blank",
        ),
        "side": fields.String(
            required="True",
            description="side dish when sip a glass of coffee",
            help="side cannot be blank",
        ),
    },
)
coffees = [
    {
        "id": 1,
        "name": "Arabica Beans",
        "origin": "Bajaregara",
        "usage": ["Drip", "Filter", "French Press"],
        "side": "Gorengan",
    },
    {
        "id": 2,
        "name": "Toraja Beans",
        "origin": "Toraja",
        "usage": ["Pour Over", "Auto Drip", "French Press"],
        "side": "Kue",
    },
]


@app.route("/login")
def token():
    expiration_date = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    token = jwt.encode(
        {"exp": expiration_date}, app.config["SECRET_KEY"], algorithm="HS256"
    )
    return token


def valid_coffee(coffee_object):
    if (
        "name" in coffee_object
        and "origin" in coffee_object
        and "usage" in coffee_object
        and "side" in coffee_object
    ):
        return True
    else:
        return False


@api.route("/")
class CoffeeList(Resource):
    def get(self):
        """
        Returns list of coffee
        """
        token = request.args.get("token")
        try:
            jwt.decode(token, app.config["SECRET_KEY"])
        except:
            return {"status": "authentication required"}, 401

        return jsonify({"coffee": Coffee.get_all()})

    @api.doc(
        Response={
            201: "Created",
            200: "OK",
            400: "Invalid argument",
            404: "Coffee not found",
            500: "Mapping key error",
        }
    )
    @api.expect(coffee_model, validate=True)
    def post(self):
        """
        Add single coffee
        """
        request_data = request.get_json()
        if valid_coffee(request_data):
            # api.payload["id"] = coffees[-1]["id"] + 1 if len(coffees) > 0 else 0
            # new_coffee = {
            #     "id": api.payload["id"],
            #     "name": request_data["name"],
            #     "origin": request_data["origin"],
            #     "usage": request_data["usage"],
            #     "side": request_data["side"],
            # }
            # coffees.append(new_coffee)
            Coffee.add_coffee(
                request_data["name"],
                request_data["origin"],
                request_data["usage"],
                request_data["side"],
            )
            response = Response(status=201, mimetype="application/json")
            response.headers["location"] = request_data["id"]
            return response
        else:
            return api.abort(400)


# returing single value
@api.route("/<int:id>")
class GetCoffeeById(Resource):
    def find_one(self, id):
        return next((b for b in coffees if b["id"] == id), None)

    @api.doc(
        response={
            200: "OK",
            400: "Invalid argument",
            404: "Coffee not found",
            500: "Mapping key error",
        },
        params={"id": "Specify the id associate with the coffee"},
    )
    def get(self, id):
        """
        return a single coffee
        """
        # match = self.find_one(id)
        match = Coffee.get_coffee(id)
        return match if match else ({"status": "Coffee Not Found 404"})

    @api.doc(
        response={
            200: "OK",
            400: "Invalid argument",
            500: "Mapping key error",
        },
        params={"id": "Specify the id associate with the coffee to update"},
    )
    @api.expect(coffee_model, validate=True)
    def put(self, id):
        request_data = request.get_json()
        """
        Update single coffee
        """
        # match = self.find_one(id)
        # if match != None:
        #     match.update(api.payload)
        #     match["id"] = id
        match = Coffee.replace_coffee(
            id,
            request_data["name"],
            request_data["origin"],
            request_data["usage"],
            request_data["side"],
        )
        return match

    @api.doc(
        response={
            200: "OK",
            400: "Invalid argument",
            500: "Mapping key error",
        },
        params={"id": "Specify the id associate with the coffee to delete"},
    )
    def delete(self, id):
        """
        Delete single coffee
        """
        # global coffees
        # match = self.find_one(id)
        # coffees = list(filter(lambda b: b["id"] != id, coffees))
        match = Coffee.delete_coffee(id)
        return match

if  __name__ == '__main__':  
    app.run(debug=True) 
