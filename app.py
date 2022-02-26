import traceback
from flask import Flask, request, json, Response


from utils import fetch_transaction_info, fetch_transaction_summary

app = Flask(__name__)


@app.route('/transaction/<transaction_id>', methods=['GET'])
def get_transaction_details(transaction_id):
    # args = request.args
    error_msg = ""
    status_code = 400

    try:        
        if transaction_id:
            data = fetch_transaction_info(transaction_id)
            if data:
                return Response(response=json.dumps(data),
                        status=200,
                        mimetype='application/json')

            else:
                error_msg = "Data not found!"
                status_code = 204                

        else:
            error_msg = "Invalid params!"
            status = 206
    
    except:
        traceback.print_exc()
        error_msg = "Something went wrong!"

    return Response(response=json.dumps({"error": error_msg}),
                                status = status_code,
                                mimetype='application/json')


@app.route('/transaction-summary-bySKU/<last_n_days>', methods=['GET'])
def get_transaction_summary_by_sku_name(last_n_days):        
    error_msg = ""
    status_code = 400

    try:                
        if last_n_days:
            data = fetch_transaction_summary(last_n_days, "sku_name")
            if data:
                return Response(response=json.dumps({"summary": data}),
                        status=200,
                        mimetype='application/json')

            else:
                error_msg = "Data not found!"
                status_code = 204                

        else:
            error_msg = "Invalid params!"
            status = 206
    
    except Exception as ex:    
        error_msg = "Something went wrong!"

    return Response(response=json.dumps({"error": error_msg}),
                                status = status_code,
                                mimetype='application/json')


@app.route('/transaction-summary-bycategory/<last_n_days>', methods=['GET'])
def get_transaction_summary_by_sku_category(last_n_days):    
    error_msg = ""
    status_code = 400

    try:        
        if last_n_days:
            data = fetch_transaction_summary(last_n_days, "sku_category")
            if data:
                return Response(response=json.dumps({"summary": data}),
                        status=200,
                        mimetype='application/json')

            else:
                error_msg = "Data not found!"
                status_code = 204                

        else:
            error_msg = "Invalid params!"
            status = 206
    
    except:        
        error_msg = "Something went wrong!"

    return Response(response=json.dumps({"error": error_msg}),
                                status = status_code,
                                mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')