package tree;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class TraversalInorder {
    List<Integer> ans = new ArrayList<>();
    public void inorder(TreeNode root){
        if (root == null) {
            return;
        }
        inorder(root.left);
        ans.add(root.val);
        inorder(root.right);
    }
    public List<Integer> inorder_(TreeNode root){
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> ans = new ArrayList<>();
        while (root != null || !stack.isEmpty()) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            TreeNode topEle = stack.pop();
            ans.add(topEle.val);
            root = topEle.right;
        }
        return ans;
    }
}
