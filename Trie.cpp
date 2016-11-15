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
#include <cassert>

using namespace std;

class TrieNode {

    public:

    int  _no; // vertex number

    char _element; // vertex name

    unordered_map<char, TrieNode*> _table; //set of vertices

    bool _leaf; // terminal character

    bool _extended; //Prefix of Prefix

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

    // Prefix Match
    // Patterns are not Prefix of Another Pattern
    bool _prefix_match_pos(int i, string& text, TrieNode* node) {

         assert(i >= 0);
         assert(node);

         if (node->_leaf) 
             return true;

         if (i >= text.length())
             return false;

         auto key = text.at(i);
         if (node->_table.find(key) != node->_table.end()) {
             //cout << "DBG key " << key << endl;
             return  _prefix_match_pos(i + 1, text, node->_table[key]);
         } else 
             return false;
    }

    // Extended Prefix Matching
    bool _prefix_match_pos_ext(int i, string& text, TrieNode* node) {

         assert(i >= 0);
         assert(node);

         if (node->_leaf || node->_extended) {
//           cout << "DBG : Found!" << endl;
             return true;
         }    

         if (i >= text.length())
             return false;

         auto key = text.at(i);
         if (node->_table.find(key) != node->_table.end()) {
//             cout << "DBG key " << key << endl;
             return  _prefix_match_pos_ext(i + 1, text, node->_table[key]);
         } else 
             return false;
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
                     node = new TrieNode(++_lastno, element, i == (n - 1));
                     table[element] = node; 
                     //if (node->_leaf)
                     //    cout << "DBG Leaf " << node->_element << endl;
                 } else {
                     node = table[element];
                     if (node->_extended) {
                         break;
                     } else if (node->_leaf) {
                         node->_extended = (i < (n - 1)) ? true : false;
                         node->_leaf = node->_extended ? false : true;
                     } else if (i == (n - 1)) 
                            node->_extended =  true;
                            
                     //if (node->_extended)
                     //    cout << "DBG Ext " << node->_element << endl;
                 }   
                 i++;
             }     
        }    

        void printTrie(void) {
            cout << "----Printing Trie Patterns----" << endl;
            _dfs(_rootp, 0);
        }    

        void prefix_match(string& text) {
            int n = text.length();
            cout << "-----Pattern Match offsets(" << text << ") ------" << endl;
            while (n--) {
                if (_prefix_match_pos(n, text, _rootp))
                    cout << "Match " << n << endl;
            }    
        }    

        void prefix_match_ext(string& text) {
            int n = text.length();
            cout << "-----Extended Pattern Match offsets(" << text << ") ------" << endl;
            while (n--) {
                if (_prefix_match_pos_ext(n, text, _rootp))
                    cout << "Match " << n << endl;
            }    
        }    
};           

int assignment01(void) {
    vector<string> pat = { "ATAGA", "ATC", "GAT"};
    Trie *t = new Trie();
    for (auto& i : pat) {
        cout << i << endl;
        t->add_pattern(i);
    }    
    t->printTrie();
    delete t;
    return 0;
}

int assignment02(void) {
    string text = "AATCGGGTTCAATCGGGGT";
    vector<string> pat = { "ATCG", "GGGT"};
    Trie *t = new Trie();
    for (auto& i : pat) {
        cout << i << endl;
        t->add_pattern(i);
    }    
    t->prefix_match(text);
    delete t;
    return 0;
}    

int assignment03(void) {
    string text = "ACATA";
    vector<string> pat = { "AT","A", "AG"};
    Trie *t = new Trie();
    for (auto& i : pat) {
        cout << i << endl;
        t->add_pattern(i);
    }    
    //t->prefix_match(text);
    t->prefix_match_ext(text);
    delete t;
    return 0;
}    

int main(void) {
    assignment01();
    assignment02();
    assignment03();
    return 0;
}    
