from neo4j import RoutingControl
## função para salvar amigos 
def add_friend(driver, name, friend_name, mother):
    driver.execute_query(

         """
        MERGE (a:Person {name: $name})
        MERGE (f:Person {name: $friend_name})
        MERGE (m:Person {name: $mother})
        MERGE (a)-[:KNOWS]->(f)->[:DAUGHTER]->(m)
        """,
        name=name,
        friend_name=friend_name,
        database_="neo4j",

    )
