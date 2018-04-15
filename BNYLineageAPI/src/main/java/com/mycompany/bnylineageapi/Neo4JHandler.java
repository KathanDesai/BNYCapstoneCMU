
package com.mycompany.bnylineageapi;
import org.neo4j.driver.v1.AuthTokens;
import org.neo4j.driver.v1.Driver;
import org.neo4j.driver.v1.GraphDatabase;
import org.neo4j.driver.v1.Session;
import org.neo4j.driver.v1.StatementResult;
import org.neo4j.driver.v1.Transaction;
import org.neo4j.driver.v1.TransactionWork;
import static org.neo4j.driver.v1.Values.parameters;

import org.json.JSONObject;

/**
 *
 * @author Kathan
 */
public class Neo4JHandler {
    public void addObject(JSONObject obj){
        System.out.println(obj);
    }
}
