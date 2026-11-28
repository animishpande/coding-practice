public class Solution {
    public int EvalRPN(string[] tokens) {
        Stack<int> s = new Stack<int>();
        foreach(string v in tokens)
        {
            if (v == "+")
            {
                s.Push(s.Pop() + s.Pop());
            }
            else if (v == "-")
            {
                int a = s.Pop();
                int b = s.Pop();
                s.Push(b - a);
            }
            else if (v == "*")
            {
                int a = s.Pop();
                int b = s.Pop();
                s.Push(a * b);
            }
            else if (v == "/")
            {
                int a = s.Pop();
                int b = s.Pop();
                s.Push((int) ((double) b / a));
            }
            else
            {
                s.Push(int.Parse(v));
            }
        }

        
        return s.Pop();
    }
}
