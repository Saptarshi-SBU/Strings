/*-----------------------------------------------------
 *
 * Coursera Assignment : 
 *
 * +)Construct a Trie from a Collection of Patterns
 * g++ -o main -std=c++11 Trie.cpp
 *
 * ----------------------------------------------------*/

#include <vector>
#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class TrieNode {

    public:

    int  _no; // vertex number

    char _element; // vertex name

    unordered_map<char, TrieNode*> _table; //set of vertices

    bool _leaf; // terminal character

    TrieNode(int no, char elem, bool is_terminal) : 
                       _element(elem), _leaf(is_terminal), _no(no) { }
    ~TrieNode() {}
};

class Trie {

    TrieNode *_rootp;

    int _lastno; // count vertices in the Trie

    // Post-Order Traversal
    void _clear(TrieNode *node) {
        if (!node)
            return;
        for (auto& i : node->_table)
            _clear(i.second);
        node->_table.clear();
        delete node;
    }

    // DFS 
    void _dfs(TrieNode *node, int ep) {
         for (auto& i : node->_table) {
             cout << ep << "->" << i.second->_no << " ";
             cout << i.first << endl;
             _dfs(i.second, i.second->_no);
         }    
    }

    public:
        Trie() { _rootp = new TrieNode(0, '$', false); _lastno = 0;}
       ~Trie() { _clear(_rootp); }
        
        void add_pattern(string s) {
             int i = 0;
             int n = s.length();
             auto node = _rootp;

             while(i < n) {
                 auto element = s.at(i); 
                 auto& table = node->_table;
                 if (table.find(element) == table.end()) {
                     node = new TrieNode(++_lastno, element, i < (n - 1));
                     table[element] = node; 
                 } else
                     node = table[element];
                 i++;
             }     
        }    

        void printTrie(void) {
            cout << "----Printing Trie Patterns----" << endl;
            _dfs(_rootp, 0);
        }    
};           

int main(void) {
    // Sample 1
    Trie *t;
    vector<string> strlist1 = { "ATA" };
    t = new Trie();
    for (auto& i : strlist1) {
        cout << i << endl;
        t->add_pattern(i);
    }    
    t->printTrie();
    delete t;
    // Sample 2
    vector<string> strlist2 = { "AT", "AG", "AC"};
    t = new Trie();
    for (auto& i : strlist2) {
        cout << i << endl;
        t->add_pattern(i);
    }    
    t->printTrie();
    delete t;
    // Sample 3
    vector<string> strlist3 = { "ATAGA", "ATC", "GAT"};
    t = new Trie();
    for (auto& i : strlist3) {
        cout << i << endl;
        t->add_pattern(i);
    }    
    t->printTrie();
    delete t;
    return 0;
}
