import json
import logging
import requests

id_map = {}
def get_nodes(node_id):
  base_url = "https://nodes-on-nodes-challenge.herokuapp.com/nodes"
  url = "{}/{}".format(base_url, node_id)
  print("Getting {}".format(url))

  resp = requests.get(url)
  body = json.loads(resp.text)

  new_nodes = []

  for item in body:
    child_nodes = item['child_node_ids']
    print("Found {} child nodes".format(len(child_nodes)))

    for child_node in child_nodes:
      if child_node not in id_map:
        id_map[child_node] = 0

      id_map[child_node] += 1

    new_nodes.extend(child_nodes)

  if new_nodes:
    get_nodes(",".join(new_nodes))

  return (max(id_map, key=id_map.get), len(id_map))

node_id = "089ef556-dfff-4ff2-9733-654645be56fe"

results = get_nodes(node_id)
most_common_node = results[0]
num_unique_nodes = results[1]

print("The most common node is: {}".format(most_common_node))
print("The total number of unique node IDs is: {}".format(num_unique_nodes))
