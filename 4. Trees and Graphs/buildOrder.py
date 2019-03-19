# You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be built. If there
# is no valid build order, return an error. 
projects = [1,2,3,4]
dependencies = [(1,2),(2,3),(4,2)]

# 1 4
#  2
#  3

def buildOrder(projects, dependencies):
	dependency_map = map_dependencies(dependencies, projects)
	build_order = []
	visited = {}
	noDependencyList = noDependencies(dependency_map)
	recursiveAddToBuild(noDependencyList, dependency_map, visited, build_order)
	return build_order

def recursiveAddToBuild(projects, dependency_map, visited, buildOrder):
	if (len(projects) == 0):
		return
	nextBuilds= []
	for project in projects:
		if project in visited.keys():
			return False
		visited[project] = True
		buildOrder.append(project)
		dependents = dependency_map[project]['dependents']
		nextProjects = nextToBuild(dependents, dependency_map)
		nextBuilds = nextBuilds + nextProjects
	recursiveAddToBuild(nextBuilds, dependency_map, visited, buildOrder)

def nextToBuild(dependents, dependency_map):
	projects = []
	for project in dependents:
		dependency_map[project]['dependency_ct'] = dependency_map[project]['dependency_ct'] - 1
		if dependency_map[project]['dependency_ct'] == 0:
			projects.append(project)
	return projects

def map_dependencies(dependencies, projects):
	dependency_map = {}
	for dependency, project in dependencies: 
		# appends this project to the list of projects that are dependent on this dependency
		dependency_map[dependency] = dependency_map.get(dependency, {'dependents': [], 'dependency_ct': 0})
		dependency_map[dependency]['dependents'].append(project)

		# increments the dependency count of this project
		dependency_map[project] = dependency_map.get(project, {'dependents': [], 'dependency_ct': 0})
		dependency_map[project]['dependency_ct'] +=1
	for project in projects:
		dependency_map[project] = dependency_map.get(project, {'dependents': [], 'dependency_ct': 0})
	return dependency_map

def noDependencies(dependency_map):
	noDependencies = []
	for project in dependency_map.keys():
		if dependency_map[project]['dependency_ct'] == 0:
			noDependencies.append(project)
	return noDependencies



# def recursiveTraverse(project, dependency_map, visited, build_order):
# 	#base case is either appending a project to the build order because it has no dependencies or False(when there is a dependency loop)
# 	if (visited.get(project, False) == True):
# 		return False
# 	visited[project] = True
# 	if (len(dependency_map.get(project, [])) == 0):
# 		remove_dependencies(dependency_map, project)
# 		build_order.append(project)
# 		return
# 	for project in dependency_map[project]:
# 		result = recursiveTraverse(project, dependency_map, visited, build_order)
# 		if (result == False):
# 			return False
# 	build_order.append(project)
# 	return

# def map_dependencies(dependencies, projects):
# 	dependency_map = {}
# 	for dependency, project in dependencies:
# 		dependency_list = dependency_map.get(project, [])
# 		dependency_list.append(dependency)
# 		dependency_map[project] = dependency_list
# 	for project in projects:
# 		dependency_map[project] = dependency_map.get(project, [])
# 	return dependency_map

# def remove_dependencies(dependency_map, projectToRemove):
# 	for project, dependencies in dependency_map.items():
# 		if projectToRemove in dependencies:
# 			dependencies.remove(projectToRemove)

# def noDependencies(dependency_map):
# 	noDependencies = []
# 	dependencies = []
# 	for project, dependencyList in dependency_map.items():
# 		if len(dependencyList) == 0:
# 			noDependencies.append(project)
# 		else:
# 			dependencies.append(project)
# 	return noDependencies + dependencies