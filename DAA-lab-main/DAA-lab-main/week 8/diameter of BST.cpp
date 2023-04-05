#include <iostream>
using namespace std;

// Define TreeNode class to represent nodes in the binary tree
class TreeNode {

public:
    int val;
    TreeNode* left;
    TreeNode* right;

    // Constructor to initialize a new node with the given value
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// Define BinaryTree class to represent the binary tree
class BinaryTree {

public:
    TreeNode* root;

    // Constructor to initialize an empty binary tree
    BinaryTree() : root(NULL) {}

    // Method to insert a new node with the given value into the binary tree
    void insert(int val) {
    
        if (root == NULL) {
        
            // if the root is null, create a new node and set it as the root
            root = new TreeNode(val);
            return;
        }
        // Traverse the tree to find the appropriate place to insert the new node
        TreeNode* cur = root;
        
        while (true) {
        
            if (val < cur->val) {
            
                if (cur->left == NULL) {
                
                    cur->left = new TreeNode(val);
                    return;
                }
                cur = cur->left;
            } 
            else {
            
                if (cur->right == NULL) {
                
                    cur->right = new TreeNode(val);
                    return;
                }
                cur = cur->right;
            }
        }
    }

    // Method to recursively count the total number of nodes in the tree
    int countNodes(TreeNode* node) {
    
        if (node == NULL) {
        
            // if the current node is null, return 0
            return 0;
        }
        // Recursively count the number of nodes in the left and right subtrees
        return 1 + countNodes(node->left) + countNodes(node->right);
    }

    // Method to count the total number of nodes in the tree (starting from the root)
    int countNodes() {
    
        return countNodes(root);
    }
};

int main() {

    // Create a new Binary Tree
    BinaryTree tree;
    
    int n;
    cout << "Enter number of nodes: ";
    cin >> n;
    
    cout << "Enter " << n << " node values:\n";
   
    for (int i = 0; i < n; i++) {
    
        int val;
        cin >> val;
        tree.insert(val);
    }
    
    int numNodes = tree.countNodes();
    
    cout << "Total number of nodes in the tree: " << numNodes << endl;
    
    return 69;
}
