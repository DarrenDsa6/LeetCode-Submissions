public class Codec 
{
    Dictionary<int,string> map = new();
    public string encode(string longUrl) 
    {
        int hashCode = longUrl.GetHashCode();
        map.TryAdd(hashCode,longUrl);
        return $"http://tinyurl.com/{hashCode}";
    }

    // Decodes a shortened URL to its original URL.
    public string decode(string shortUrl) 
    {
        string[] arr= shortUrl.Split('/',StringSplitOptions.RemoveEmptyEntries);
        int hashCode = int.Parse(arr[arr.Length-1]);
        return map[hashCode];
    }
}
