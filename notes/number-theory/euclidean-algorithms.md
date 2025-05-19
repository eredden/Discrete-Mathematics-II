### GREATEST COMMON DENOMINATOR THEOREM:
Let x and y be two positive integers. Then **GCD(x, y) = GCD(y mod x, x).**


### EUCLIDEAN ALGORITHM:
The simplification of calculating the GCD for two integers using modulo operations can be repeated. y is set to the value of x, x is set to the remainder, and then the **modulo operations repeat until y mod x = 0**. Once y mod x = 0, the y is a multiple of x and **GCD(x, y) = x**.

```
Input: Two positive integers, x and y.
Output: GCD(x, y).

If ( x > y )
      Swap x and y.
r := y mod x.

While ( r ≠ 0 )
      y := x
      x := r
      r := y mod x.
End-while

Return( x )
``` 


### EXTENDED EUCLIDEAN ALGORITHM:
The GCD of x and y can be expressed as a linear combination of x and y.
Let x and y be integers, then there are integers s and t such that:
**GCD(x, y) = sx + ty**

Ex. GCD(874, 2415) = (s * 874) + (t * 2415)

Recall that the equation used for division and modulo operations is y = qx + r. We can modify this to solve for r, such that r = y - qx. We can eliminate q by substituting it with (y div x), such that:
r = y - (y div x) * x

With this knowledge in hand, you can find the Bezout coefficients (s, t) of the linear combination of x and y by using the tabular framework shown below.

### EXTENDED EUCLIDEAN ALGORITHM TABULAR EXAMPLE:

The following table shows how the extended Euclidean algorithm proceeds with input <span class="nowrap"><span style="color:green;">240</span></span> and <span class="nowrap"><span style="color:green;">46</span></span>. The greatest common divisor is the last non zero entry, <span class="nowrap"><span style="color: red;">2</span></span> in the column "remainder". The computation stops at row 6, because the remainder in it is <span class="nowrap"><span style="color: red;">0</span></span>. <strong>Bézout coefficients appear in the last two columns of the second-to-last row in pink.</strong> In fact, it is easy to verify that <span class="nowrap"><span style="color:magenta">−9</span> × <span style="color:green;">240</span> + <span style="color:magenta">47</span> × <span style="color:green;">46</span> = <span style="color: red;">2</span></span>. Finally the last two entries  <span class="nowrap"><span style="color:cyan">23</span></span> and <span class="nowrap"><span style="color:cyan">−120</span></span> of the last row are, up to the sign, the quotients of the input <span class="nowrap"><span style="color:green;">46</span></span> and <span class="nowrap"><span style="color:green;">240</span></span> by the greatest common divisor <span class="nowrap"><span style="color: red;">2</span></span>.

<table style="text-align:right;">
  <tbody>
    <tr>
      <th>index <i>i</i>
      </th>
      <th>
        <span style="color:blue">quotient <i>q</i>
          <sub>
            <i>i</i>−1 </sub>
        </span>
      </th>
      <th>
        <span style="color:olive">Remainder <i>r</i>
          <sub>
            <i>i</i>
          </sub>
        </span>
      </th>
      <th>
        <span style="color:#964B00">
          <i>s</i>
          <sub>
            <i>i</i>
          </sub>
        </span>
      </th>
      <th>
        <i>t</i>
        <sub>
          <i>i</i>
        </sub>
      </th>
    </tr>
    <tr>
      <td>0</td>
      <td></td>
      <td>
        <span style="color:green;">240</span>
      </td>
      <td>
        <span style="color:#964B00">1</span>
      </td>
      <td>0 </td>
    </tr>
    <tr>
      <td>1</td>
      <td></td>
      <td>
        <span style="color:green;">46</span>
      </td>
      <td>
        <span style="color:#964B00">0</span>
      </td>
      <td>1 </td>
    </tr>
    <tr>
      <td>2</td>
      <td>
        <span style="color:green;">240</span> ÷ <span style="color:green;">46</span> = <span style="color:blue">5</span>
      </td>
      <td>
        <span style="color:green;">240</span> − <span style="color:blue">5</span> × <span style="color:green;">46</span> = <span style="color:olive">10</span>
      </td>
      <td>
        <span style="color:#964B00">1</span> − <span style="color:blue">5</span> × <span style="color:#964B00">0</span> = <span style="color:#964B00">1</span>
      </td>
      <td>0 − <span style="color:blue">5</span> × 1 = −5 </td>
    </tr>
    <tr>
      <td>3</td>
      <td>
        <span style="color:green;">46</span> ÷ <span style="color:olive">10</span> = <span style="color:blue">4</span>
      </td>
      <td>
        <span style="color:green;">46</span> − <span style="color:blue">4</span> × <span style="color:olive">10</span> = <span style="color:olive">6</span>
      </td>
      <td>
        <span style="color:#964B00">0</span> − <span style="color:blue">4</span> × <span style="color:#964B00">1</span> = <span style="color:#964B00">−4</span>
      </td>
      <td>1 − <span style="color:blue">4</span> × −5 = 21 </td>
    </tr>
    <tr>
      <td>4</td>
      <td>
        <span style="color:olive">10</span> ÷ <span style="color:olive">6</span> = <span style="color:blue">1</span>
      </td>
      <td>
        <span style="color:olive">10</span> − <span style="color:blue">1</span> × <span style="color:olive">6</span> = <span style="color:olive">4</span>
      </td>
      <td>
        <span style="color:#964B00">1</span> − <span style="color:blue">1</span> × <span style="color:#964B00">−4</span> = <span style="color:#964B00">5</span>
      </td>
      <td>−5 − <span style="color:blue">1</span> × 21 = −26 </td>
    </tr>
    <tr>
      <td>5</td>
      <td>
        <span style="color:olive">6</span> ÷ <span style="color:olive">4</span> = <span style="color:blue">1</span>
      </td>
      <td>
        <span style="color:olive">6</span> − <span style="color:blue">1</span> × <span style="color:olive">4</span> = <span style="color: red;">2</span>
      </td>
      <td>
        <span style="color:#964B00">−4</span> − <span style="color:blue">1</span> × <span style="color:#964B00">5</span> = <span style="color:magenta">−9</span>
      </td>
      <td>21 − <span style="color:blue">1</span> × −26 = <span style="color:magenta">47</span>
      </td>
    </tr>
    <tr>
      <td>6</td>
      <td>
        <span style="color:olive">4</span> ÷ <span style="color:olive">2</span> = <span style="color:blue">2</span>
      </td>
      <td>
        <span style="color:olive">4</span> − <span style="color:blue">2</span> × <span style="color:olive">2</span> = <span style="color: red;">0</span>
      </td>
      <td>
        <span style="color:#964B00">5</span> − <span style="color:blue">2</span> × <span style="color:#964B00">−9</span> = <span style="color:cyan">23</span>
      </td>
      <td>−26 − <span style="color:blue">2</span> × 47 = <span style="color:cyan">−120</span>
      </td>
    </tr>
  </tbody>

<table style="text-align:right;">
  <tbody>
    <tr>
      <th>index <i>i</i>
      </th>
      <th>
        <span style="color:blue">quotient <i>q</i>
          <sub>
            <i>i</i>−1 </sub>
        </span>
      </th>
      <th>
        <span style="color:olive">Remainder <i>r</i>
          <sub>
            <i>i</i>
          </sub>
        </span>
      </th>
      <th>
        <span style="color:#964B00">
          <i>s</i>
          <sub>
            <i>i</i>
          </sub>
        </span>
      </th>
      <th>
        <i>t</i>
        <sub>
          <i>i</i>
        </sub>
      </th>
    </tr>
    <tr>
      <td>0</td>
      <td></td>
      <td>
          <span style="color:green">a</span> 
      </td>
      <td>
        <span style="color:#964B00">1</span>
      </td>
      <td>0</td>
    </tr>
    <tr>
      <td>1</td>
      <td></td>
      <td>
          <span style="color:green">b</span> 
      </td>
      <td>
        <span style="color:#964B00">0</span>
      </td>
      <td>1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>
        <span style="color:blue">q <sub>1</sub>
        </span>
      </td>
      <td>
          <span style="color:green">a</span> 
        - <span style="color:blue">q <sub>2</sub></span>
        × <span style="color:green">b</span>
        = <span style="color:olive;">r <sub>2</sub>
        </span>
      </td>
      <td>
        <span style="color:#964B00">s <sub>0</sub>
        </span> - <span style="color:blue">q <sub>1</sub>
        </span> × <span style="color:#964B00">s <sub>1</sub>
        </span> = <span style="color:#964B00">s <sub>2</sub>
        </span>
      </td>
      <td>t <sub>0</sub> - <span style="color:blue">q <sub>1</sub>
        </span> × t <sub>1</sub> = t <sub>2</sub>
      </td>
    </tr>
    <tr>
      <td>3</td>
      <td>
        <span style="color:blue">q <sub>2</sub>
        </span>
      </td>
      <td>
          <span style="color:green">b</span> 
        - <span style="color:blue">q <sub>3</sub></span>
        × <span style="color:olive">r <sub>2</sub></span>
        = <span style="color:olive;">r <sub>3</sub>
        </span>
      </td>
      <td>
        <span style="color:#964B00">s <sub>1</sub>
        </span> - <span style="color:blue">q <sub>2</sub>
        </span> × <span style="color:#964B00">s <sub>2</sub>
        </span> = <span style="color:#964B00">s <sub>3 </span>
      </td>
      <td>t <sub>1</sub> - <span style="color:blue">q <sub>2</sub>
        </span> × t <sub>2</sub> = t <sub>3</sub>
      </td>
    </tr>
    <tr>
      <td>4</td>
      <td>
        <span style="color:blue">q <sub>3</sub>
        </span>
      </td>
      <td>
          <span style="color:olive">r <sub>2</sub></span> 
        - <span style="color:blue">q <sub>i</sub></span>
        × <span style="color:olive">r <sub>3</sub></span>
        = <span style="color:olive;">r <sub>4</sub>
        </span>
      </td>
      <td>
        <span style="color:#964B00">s <sub>2</sub>
        </span> - <span style="color:blue">q <sub>3</sub>
        </span> × <span style="color:#964B00">s <sub>3</sub>
        </span> = <span style="color:#964B00">s <sub>4 </span>
      </td>
      <td>t <sub>2</sub> - <span style="color:blue">q <sub>3</sub>
        </span> × t <sub>3</sub> = t <sub>4</sub>
      </td>
    </tr>
    <tr>
      <td>5</td>
      <td>
        <span style="color:blue">q <sub>4</sub>
        </span>
      </td>
      <td>
          <span style="color:olive">r <sub>3</sub></span> 
        - <span style="color:blue">q <sub>i</sub></span>
        × <span style="color:olive">r <sub>4</sub></span>
        = <span style="color:red;">r <sub>5</sub></span>
      </td>
      <td>
        <span style="color:#964B00">s <sub>3</sub>
        </span> - <span style="color:blue">q <sub>4</sub>
        </span> × <span style="color:#964B00">s <sub>4</sub>
        </span> = <span style="color:magenta">s <sub>5 </span>
      </td>
      <td>t <sub>3</sub> - <span style="color:blue">q <sub>4</sub>
        </span> × t <sub>4</sub> = <span style="color:magenta">t <sub>5</sub></span>
      </td>
    </tr>
    <tr>
      <td>6</td>
      <td>
        <span style="color:blue">q <sub>5</sub>
        </span>
      </td>
      <td>
          <span style="color:olive">r <sub>4</sub></span> 
        - <span style="color:blue">q <sub>i</sub></span>
        × <span style="color:red">r <sub>5</sub></span>
        = <span style="color:red;">r <sub>6</sub></span>
        </span>
      </td>
      <td>
        <span style="color:#964B00">s <sub>4</sub>
        </span> - <span style="color:blue">q <sub>5</sub>
        </span> × <span style="color:#964B00">s <sub>5</sub>
        </span> = <span style="color:#964B00">s <sub>6 </span>
      </td>
      <td>
        t <sub>4</sub> - <span style="color:blue">q <sub>5</sub></span> × t <sub>5</sub> = t <sub>6</sub>
      </td>
    </tr>
  </tbody>
</table>