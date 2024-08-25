public class Solution {
    public string Interpret(string command) {
        command = command.Replace("()","o");
        command = command.Replace("(al)","al");
        return command;
    }
}
