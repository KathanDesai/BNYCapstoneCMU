/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author ziruihua
 */
import java.util.HashMap;
import org.neo4j.driver.v1.AuthTokens;
import org.neo4j.driver.v1.Driver;
import org.neo4j.driver.v1.GraphDatabase;
import org.neo4j.driver.v1.Session;
import org.neo4j.driver.v1.StatementResult;
import org.neo4j.driver.v1.Transaction;
import org.neo4j.driver.v1.TransactionWork;

import static org.neo4j.driver.v1.Values.parameters;

public class HelloWorldExample implements AutoCloseable {

    private final Driver driver;

    public HelloWorldExample(String uri, String user, String password) {
        driver = GraphDatabase.driver(uri, AuthTokens.basic(user, password));
    }

    @Override
    public void close() throws Exception {
        driver.close();
    }
    /**
     * Add a node into system
     * @param name, name of the node, there will be more parameters
     */

    private void addNode(String name) {
        // Sessions are lightweight and disposable connection wrappers.
        try (Session session = driver.session()) {
            try (Transaction tx = session.beginTransaction()) {
                tx.run("MERGE (a:Role {name: {x}, other:'billon'})", parameters("x", name));
                tx.success();  // Mark this write as successful.
                System.out.println("Done");
                
            }
        }
    }
    /**
     * Add a relationship between source and target system
     * @param source
     * @param target 
     */

    private void addRelationship(String source, String target) {
        // Sessions are lightweight and disposable connection wrappers.
        try (Session session = driver.session()) {

            try (Transaction tx = session.beginTransaction()) {
                tx.run("MATCH (u:Role {name:'Process'}), (r:Role {name:'Payment'})\n" +
"                       CREATE (u)-[:USE]->(r)");
//                tx.run("CREATE (Ray:Role {name: {x}})", parameters("x", name));
                
                tx.success();  // Mark this write as successful.
                System.out.println("Done");
            }
        }
    }
    /**
     * Query if there is relationship between two systems
     * @param source source system
     * @param target target system
     */
    private void query(String source, String target) {
        
    }

    public static void main(String... args) throws Exception {
        try (HelloWorldExample greeter = new HelloWorldExample("bolt://localhost:7687", "zirui", "123")) {
            greeter.addNode("Payment");
            greeter.addNode("Process");
            greeter.addRelationship("Payment", "Process");
        }
    }
}
