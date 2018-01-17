import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
public class BrowserAutomation 
{ 
	public static void main(String[] args) 
	{ 
		WebDriver driver=new FirefoxDriver(); 
		driver.get("http://www.facebook.com"); 
		driver.findElement(By.id("email")).sendKeys("yourUsername"); 
		driver.findElement(By.id("pass")).sendKeys("yourPassword"); 
		driver.findElement(By.id("u_0_2")).click(); 
	} 
}
