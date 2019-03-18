# You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be built. If there
# is no valid build order, return an error. 

def buildOrder(projects, dependencies):
	dependency_map = map_dependencies(dependencies, projects)
	build_order = []
	visited = {}
	noDependencyList = noDependencies(dependency_map)
	for project in noDependencyList:
		if visited.get(project, False) == False:
			result = recursiveTraverse(project, dependency_map, visited, build_order)
			if result == False:
				return False
	return build_order



def recursiveTraverse(project, dependency_map, visited, build_order):
	#base case is either appending a project to the build order because it has no dependencies or False(when there is a dependency loop)
	if (visited.get(project, False) == True):
		return False
	visited[project] = True
	if (len(dependency_map.get(project, [])) == 0):
		remove_dependencies(dependency_map, project)
		build_order.append(project)
		return
	for project in dependency_map[project]:
		result = recursiveTraverse(project, dependency_map, visited, build_order)
		if (result == False):
			return False
	build_order.append(project)
	return

def map_dependencies(dependencies, projects):
	dependency_map = {}
	for dependency, project in dependencies:
		dependency_list = dependency_map.get(project, [])
		dependency_list.append(dependency)
		dependency_map[project] = dependency_list
	for project in projects:
		dependency_map[project] = dependency_map.get(project, [])
	return dependency_map

def remove_dependencies(dependency_map, projectToRemove):
	for project, dependencies in dependency_map.items():
		if projectToRemove in dependencies:
			dependencies.remove(projectToRemove)

def noDependencies(dependency_map):
	noDependencies = []
	dependencies = []
	for project, dependencyList in dependency_map.items():
		if len(dependencyList) == 0:
			noDependencies.append(project)
		else:
			dependencies.append(project)
	return noDependencies + dependencies