import anvil.server
import anvil.http
import psycopg2
import psycopg2.extras
import json
import requests


def connect():
  connection = psycopg2.connect(dbname='postgres',
                                host='localhost',
                                port='5432',
                                user='postgres',
                                password='simple')
  return connection


@anvil.server.callable
def get_merchants():
  conn = connect()
  with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
    cur.execute("SELECT count(merchant) FROM pipeline_output.pipeline_results")
    return cur.fetchall()


@anvil.server.callable
def call_txn_api(descriptor="GOOGLE *WM Max   LLC855-836-3987 CA", amount=24.32):
    data = [
        {
            "transactionReferenceId": "1316215c-7395-44c8-86b1-df4b838fdb8e1",
            "transactionDescription": descriptor,
            "merchantCategoryCode": 5541,
            "accountReferenceId": "f7debe91-9d8f-4500-9709-aac1d5d2ff6d",
            "transactionAmount": amount,
            "transactionDateTime": "2023-10-09T04:20:14.506925Z",
            "merchantCountry": "USA",
            "transactionCurrency": "USD"
        }
    ]


    try:
        response = anvil.http.request(
            url="http://127.0.0.1:5000/v2/cc/enriched-transactions",
            method="POST",
            data=data,
            json=True
        )

        return response

    except anvil.http.HttpError as e:
        return f"{e} -> {e.content}"
    except Exception as e:
        return f"An error occurred: {e}"

@anvil.server.callable
def call_insights_api(account_id, time_period, subscription_type):
    url = "http://127.0.0.1:5000/v1/insights/subscription_payments"
    headers = {'Content-Type': 'application/json'}
    data = {
        "accountId": account_id,
        "timePeriod": time_period,
        "subscriptionType": subscription_type
    }

    def format_subscription_details_as_html(response_json):
        html_output = "<ul>"

        for item in response_json['results']:
            merchant = item['merchant']
            last_amount = item['last_amount']
            html_output += f"<li>{merchant} - last charged ${last_amount} </li>"

        html_output += "</ul>"
        return html_output

    try:
        response = requests.get(url, headers=headers, json=data)
        return format_subscription_details_as_html(response.json())
    except requests.exceptions.RequestException as e:
        return str(e)

# @anvil.server.callable
# def call_insights_api(request):
#     data = json.dumps({
#         "accountId": "000d5572aab9fb634534d78a9535189b",
#         "timePeriod": "l3m",
#         "subscriptionType": "all"
#     })
#
#     headers = {"Access-Control-Allow-Origin": "*",
#                'Access-Control-Request-Method': '*',
#                "Access-Control-Allow-Methods": 'POST, PUT, DELETE, GET, OPTIONS',
#                'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, Authorization',
#                'Content-Type': 'application/json'
#                }
#
#     try:
#         response = anvil.http.request(
#             url="http://127.0.0.1:5000/v1/insights/subscription_payments",
#             method="GET",
#             data=data,
#             headers=headers
#         )
#
#         return response
#
#     except anvil.http.HttpError as e:
#         return f"{e} -> {e.content}"
#     except Exception as e:
#         return f"An error occurred: {e}"
#
