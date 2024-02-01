from math import sqrt
from heapq import heappop, heappush


def is_point_in_box(box, point):
    x1, x2, y1, y2 = box
    p1, p2 = point

    x_is_in = False
    y_is_in = False

    if x1 <= p1 and x2 >= p1:
        x_is_in = True
    if y1 <= p2 and y2 >= p2:
        y_is_in = True

    return x_is_in and y_is_in


def euclidean_distance(p1, p2):
    return sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


def find_path(source_point, destination_point, mesh):

    """
    Searches for a path from source_point to destination_point through the mesh

    Args:
        source_point: starting point of the pathfinder
        destination_point: the ultimate goal the pathfinder must reach
        mesh: pathway constraints the path adheres to

    Returns:

        A path (list of points) from source_point to destination_point if exists
        A list of boxes explored by the algorithm
    """

    # print("Source Point: " + str(source_point))
    # print("Destination Point: " + str(destination_point))

    path = []
    boxes = {}
    source_box = None
    destination_box = None

    # Scan through the list of boxes to find which contains the source point 
    # and which contains the destination point.
    for box in mesh['boxes']:
        if box not in boxes and is_point_in_box(box, source_point):
            source_box = box
            # print(source_box)
        if box not in boxes and is_point_in_box(box, destination_point):
            destination_box = box
            # print(destination_box)

    if (source_box is None) or (destination_box is None):
        print("No Path!")
        return [], []

    #   return path, boxes.keys()

    dist = {}
    prev = {}
    box_coords = {}

    dist[source_box] = 0
    prev[source_box] = None
    box_coords[source_box] = source_point

    priorityQueue = []
    heappush(priorityQueue, (dist[source_box], source_box))

    adj = mesh["adj"]

    while priorityQueue:

        current_cost, current_pos = heappop(priorityQueue)

        if current_pos == destination_box:
            path = [box_coords[current_pos], destination_point]

            back_box = prev[current_pos]
            back_coord = box_coords[current_pos]

            while back_box is not None:
                path.insert(0, box_coords[back_box])
                back_box = prev.get(back_box)

                if back_box is not None:
                    back_coord = box_coords[back_box]
                    print(back_coord)

            path.append(destination_point)

            return path, boxes.keys()

        for neighbor in adj[current_pos]:

            boxes[neighbor] = current_pos

            xRange = [max(current_pos[0], neighbor[0]),
                      min(current_pos[1], neighbor[1])]
            yRange = [max(current_pos[2], neighbor[2]),
                      min(current_pos[3], neighbor[3])]

            firstCost = euclidean_distance(
                (xRange[0], yRange[0]), box_coords[current_pos])
            secondCost = euclidean_distance(
                (xRange[1], yRange[1]), box_coords[current_pos])

            if firstCost <= secondCost:
                finalCost = firstCost
                finalPoint = (xRange[0], yRange[0])
            else:
                finalCost = secondCost
                finalPoint = (xRange[1], yRange[1])

            alt = current_cost + finalCost
            if neighbor not in dist or alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = current_pos
                box_coords[neighbor] = finalPoint
                heappush(priorityQueue, (alt, neighbor))
    return None
