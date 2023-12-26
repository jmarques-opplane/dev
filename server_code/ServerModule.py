import anvil.server
import anvil.http
import psycopg2
import psycopg2.extras


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
def call_txn_api(body):
  anvil.http.request(url="https://127.0.0.1:5000/health",
                    method="POST",
                    data=body,
                      headers={"Access-Control-Allow-Origin": "*",
                               'Access-Control-Request-Method': '*',
                               "Access-Control-Allow-Methods": 'POST, PUT, DELETE, GET, OPTIONS',
                               'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
                               },
                     json=True)
