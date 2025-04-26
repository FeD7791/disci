from scipy.spatial import Voronoi, ConvexHull

def _simple_voronoi_grid_maker(points):
    vor = Voronoi(points)

    volumes = []
    centers = []

    for i in range(len(points)):
        region_index = vor.point_region[i]
        region = vor.regions[region_index]

        if -1 not in region and len(region) > 3:  # bounded and enough vertices
            try:
                vertices = vor.vertices[region]
                hull = ConvexHull(vertices)
                volumes.append(hull.volume)
                centers.append(np.mean(vertices, axis=0))  # centroid of region
            except:
                volumes.append(np.nan)
                centers.append(np.full(points.shape[1], np.nan))
        else:
            volumes.append(np.nan)
            centers.append(np.full(points.shape[1], np.nan))  # same shape as a point

    return vor, np.array(volumes), np.array(centers)