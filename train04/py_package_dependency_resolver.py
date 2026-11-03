"""

"
Forbidden built-ins / modules: graphlib.TopologicalSorter.
Use only permitted built-in functions to avoid getting 0 on exam day.
"

Write a function that determines a valid package installation order by resolving dependencies. Use topological sorting to ensure dependencies are installed before the packages that require them.

The function should:
- Take a dictionary where keys are package names and values are lists of dependencies
- Return packages in installation order (dependencies first)
- Return empty list if no valid order exists (circular dependencies)
- Handle empty input and isolated dependency chains
- Ignore references to packages not in the input dictionary

Algorithm requirements:
- Use topological sorting (e.g., Kahn's algorithm)
- Process packages with no remaining dependencies first
- Ensure deterministic output when multiple valid orders exist

Edge cases to handle:
- Empty input: return empty list
- Packages with no dependencies: include in output first
- Multiple independent chains: process all chains
- Circular dependencies: return empty list
- Non-existent dependencies: ignore missing packages
- Self-dependencies: return empty list

Notes:
- For deterministic output, process packages alphabetically when choices exist
- A package cannot be installed until all its dependencies are installed
- If any circular dependency exists, no valid installation order is possible

package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []})
-> ["driver", "database", "app"]

package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]})
-> ["A", "B", "C"]

package_dependency_resolver({})
-> []

package_dependency_resolver({"X": ["Y"], "Y": ["X"]})
-> []

package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]})
-> ["api", "web", "backend", "frontend"]

"""



def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    if not packages:
        return []

    # Number of dependencies for each package
    indegree = {pkg: 0 for pkg in packages}

    # Reverse dependency graph
    dependents = {pkg: [] for pkg in packages}
    for pkg, deps in packages.items():
        for dep in deps:
            if dep in packages:
                indegree[pkg] += 1
                dependents[dep].append(pkg)

    # Start with packages having no dependencies
    queue = sorted(pkg for pkg in packages if indegree[pkg] == 0)
    result = []
    while queue:
        current = queue.pop(0)
        result.append(current)
        for dependent in dependents[current]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                queue.append(dependent)
        queue.sort()

    # If not all packages were installed, there's a cycle
    if len(result) != len(packages):
        return []
    return result



def main():
    print("1", package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []}))
    print("2", package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]}))
    print("3", package_dependency_resolver({}))
    print("4", package_dependency_resolver({"X": ["Y"], "Y": ["X"]}))
    print("5", package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}))


if __name__ == "__main__":
    main()
