import re

def main():
    for i in range(1, 10):
        k = 1 << i
        print(f'module or_scan_{k}(a, z);')

        print(f'   input [{k-1}:0] a;')
        print(f'   output [{k-1}:0] z;')


        if k == 2:
            print(f'   assign z[0] = a[0];')
            print(f'   assign z[1] = a[1] | z[0];')
        else:
            print(f'   wire [{k-1}:{k//2}] tmp;')
            print(f'   or_scan_{k//2} u0(.a(a[{k//2-1}:0]), .z(z[{k//2-1}:0]));')
            print(f'   or_scan_{k//2} u1(.a(a[{k-1}:{k//2}]), .z(tmp));')
            print(f'   assign z[{k-1}:{k//2}] = tmp | {{{k//2}{{z[{k//2-1}]}}}};')


        print(f'endmodule')
        print()


    
    # one hot mux
    for i in range(1, 10):
        k = 1 << i
        print(f'module one_hot_mux_{k}(s, d, z);')

        print(f'   input [{k-1}:0] s;')
        print(f'   input [{k-1}:0] d;')
        print(f'   output z;')

        if k == 1:
            print(f'   assign z[0] = s[0] & d[0];')
        else:
            print(f'   wire z0, z1;')
            print(f'   one_hot_mux_{k//2} u0(.s(s[{k//2-1}:0]), .d(d[{k//2-1}:0]), .z(z0));')
            print(f'   one_hot_mux_{k//2} u1(.s(s[{k-1}:{k//2-1}]), .d(d[{k-1}:{k//2-1}]), .z(z1));')
            print(f'   assign z = z0 | z1;')


        print(f'endmodule')
        print()

    # priority mux

    k = 512
    print(f'module priority_mux_{k}(s, d, z);')
    print(f'   input [{k-1}:0] s;')
    print(f'   input [{k-1}:0] d;')
    print(f'   output [{k-1}:0] z;')
    print(f'   wire [{k-1}:0] a;')
    print(f'   wire [{k-1}:0] b;')

    print(f'   or_scan_{k} u0(.a(s), .z(a));')

    print(f'   assign b = a & {{~a[{k-2}:1], 1\'b1}};')

    print(f'   one_hot_mux_{k} u1(.s(b), .d(d), .z(z));')    

    print(f'endmodule')
    print()


    for i in range(0, 10):
        k = 1 << i

        print(f'module alt_priority_mux_{k}(s, d, ss, dd);')
        print(f'   input [{k-1}:0] s;')
        print(f'   input [{k-1}:0] d;')
        print(f'   output ss;')
        print(f'   output dd;')

        if k == 1:
            print(f'   assign ss = s;')
            print(f'   assign dd = d;')
        else:
            print(f'   wire ss0;')
            print(f'   wire ss1;')
            print(f'   wire dd0;')
            print(f'   wire dd1;')
            print(f'   alt_priority_mux_{k//2} u0(.s(s[{k//2-1}:0]), .d(d[{k//2-1}:0]), .ss(ss0), .dd(dd0));')
            print(f'   alt_priority_mux_{k//2} u1(.s(s[{k-1}:{k//2}]), .d(d[{k-1}:{k//2}]), .ss(ss1), .dd(dd1));')
            print(f'   assign ss = ss0 | ss1;')
            print(f'   assign dd = ss0 & dd0 | ~ss0 & ss1 & dd1;')


        print(f'endmodule')
        print()


def driver():
    txt = """\
                 (N1568)? valid[0] :
                 (N1570)? valid[1] :
                 (N1572)? valid[2] :
                 (N1574)? valid[3] :
                 (N1576)? valid[4] :
                 (N1578)? valid[5] :
                 (N1580)? valid[6] :
                 (N1582)? valid[7] :
                 (N1584)? valid[8] :
                 (N1586)? valid[9] :
                 (N1588)? valid[10] :
                 (N1590)? valid[11] :
                 (N1592)? valid[12] :
                 (N1594)? valid[13] :
                 (N1596)? valid[14] :
                 (N1598)? valid[15] :
                 (N1600)? valid[16] :
                 (N1602)? valid[17] :
                 (N1604)? valid[18] :
                 (N1606)? valid[19] :
                 (N1608)? valid[20] :
                 (N1610)? valid[21] :
                 (N1612)? valid[22] :
                 (N1614)? valid[23] :
                 (N1616)? valid[24] :
                 (N1618)? valid[25] :
                 (N1620)? valid[26] :
                 (N1622)? valid[27] :
                 (N1624)? valid[28] :
                 (N1626)? valid[29] :
                 (N1628)? valid[30] :
                 (N1630)? valid[31] :
                 (N1632)? valid[32] :
                 (N1634)? valid[33] :
                 (N1636)? valid[34] :
                 (N1638)? valid[35] :
                 (N1640)? valid[36] :
                 (N1642)? valid[37] :
                 (N1644)? valid[38] :
                 (N1646)? valid[39] :
                 (N1648)? valid[40] :
                 (N1650)? valid[41] :
                 (N1652)? valid[42] :
                 (N1654)? valid[43] :
                 (N1656)? valid[44] :
                 (N1658)? valid[45] :
                 (N1660)? valid[46] :
                 (N1662)? valid[47] :
                 (N1664)? valid[48] :
                 (N1666)? valid[49] :
                 (N1668)? valid[50] :
                 (N1670)? valid[51] :
                 (N1672)? valid[52] :
                 (N1674)? valid[53] :
                 (N1676)? valid[54] :
                 (N1678)? valid[55] :
                 (N1680)? valid[56] :
                 (N1682)? valid[57] :
                 (N1684)? valid[58] :
                 (N1686)? valid[59] :
                 (N1688)? valid[60] :
                 (N1690)? valid[61] :
                 (N1692)? valid[62] :
                 (N1694)? valid[63] :
                 (N1696)? valid[64] :
                 (N1698)? valid[65] :
                 (N1700)? valid[66] :
                 (N1702)? valid[67] :
                 (N1704)? valid[68] :
                 (N1706)? valid[69] :
                 (N1708)? valid[70] :
                 (N1710)? valid[71] :
                 (N1712)? valid[72] :
                 (N1714)? valid[73] :
                 (N1716)? valid[74] :
                 (N1718)? valid[75] :
                 (N1720)? valid[76] :
                 (N1722)? valid[77] :
                 (N1724)? valid[78] :
                 (N1726)? valid[79] :
                 (N1728)? valid[80] :
                 (N1730)? valid[81] :
                 (N1732)? valid[82] :
                 (N1734)? valid[83] :
                 (N1736)? valid[84] :
                 (N1738)? valid[85] :
                 (N1740)? valid[86] :
                 (N1742)? valid[87] :
                 (N1744)? valid[88] :
                 (N1746)? valid[89] :
                 (N1748)? valid[90] :
                 (N1750)? valid[91] :
                 (N1752)? valid[92] :
                 (N1754)? valid[93] :
                 (N1756)? valid[94] :
                 (N1758)? valid[95] :
                 (N1760)? valid[96] :
                 (N1762)? valid[97] :
                 (N1764)? valid[98] :
                 (N1766)? valid[99] :
                 (N1768)? valid[100] :
                 (N1770)? valid[101] :
                 (N1772)? valid[102] :
                 (N1774)? valid[103] :
                 (N1776)? valid[104] :
                 (N1778)? valid[105] :
                 (N1780)? valid[106] :
                 (N1782)? valid[107] :
                 (N1784)? valid[108] :
                 (N1786)? valid[109] :
                 (N1788)? valid[110] :
                 (N1790)? valid[111] :
                 (N1792)? valid[112] :
                 (N1794)? valid[113] :
                 (N1796)? valid[114] :
                 (N1798)? valid[115] :
                 (N1800)? valid[116] :
                 (N1802)? valid[117] :
                 (N1804)? valid[118] :
                 (N1806)? valid[119] :
                 (N1808)? valid[120] :
                 (N1810)? valid[121] :
                 (N1812)? valid[122] :
                 (N1814)? valid[123] :
                 (N1816)? valid[124] :
                 (N1818)? valid[125] :
                 (N1820)? valid[126] :
                 (N1822)? valid[127] :
                 (N1824)? valid[128] :
                 (N1826)? valid[129] :
                 (N1828)? valid[130] :
                 (N1830)? valid[131] :
                 (N1832)? valid[132] :
                 (N1834)? valid[133] :
                 (N1836)? valid[134] :
                 (N1838)? valid[135] :
                 (N1840)? valid[136] :
                 (N1842)? valid[137] :
                 (N1844)? valid[138] :
                 (N1846)? valid[139] :
                 (N1848)? valid[140] :
                 (N1850)? valid[141] :
                 (N1852)? valid[142] :
                 (N1854)? valid[143] :
                 (N1856)? valid[144] :
                 (N1858)? valid[145] :
                 (N1860)? valid[146] :
                 (N1862)? valid[147] :
                 (N1864)? valid[148] :
                 (N1866)? valid[149] :
                 (N1868)? valid[150] :
                 (N1870)? valid[151] :
                 (N1872)? valid[152] :
                 (N1874)? valid[153] :
                 (N1876)? valid[154] :
                 (N1878)? valid[155] :
                 (N1880)? valid[156] :
                 (N1882)? valid[157] :
                 (N1884)? valid[158] :
                 (N1886)? valid[159] :
                 (N1888)? valid[160] :
                 (N1890)? valid[161] :
                 (N1892)? valid[162] :
                 (N1894)? valid[163] :
                 (N1896)? valid[164] :
                 (N1898)? valid[165] :
                 (N1900)? valid[166] :
                 (N1902)? valid[167] :
                 (N1904)? valid[168] :
                 (N1906)? valid[169] :
                 (N1908)? valid[170] :
                 (N1910)? valid[171] :
                 (N1912)? valid[172] :
                 (N1914)? valid[173] :
                 (N1916)? valid[174] :
                 (N1918)? valid[175] :
                 (N1920)? valid[176] :
                 (N1922)? valid[177] :
                 (N1924)? valid[178] :
                 (N1926)? valid[179] :
                 (N1928)? valid[180] :
                 (N1930)? valid[181] :
                 (N1932)? valid[182] :
                 (N1934)? valid[183] :
                 (N1936)? valid[184] :
                 (N1938)? valid[185] :
                 (N1940)? valid[186] :
                 (N1942)? valid[187] :
                 (N1944)? valid[188] :
                 (N1946)? valid[189] :
                 (N1948)? valid[190] :
                 (N1950)? valid[191] :
                 (N1952)? valid[192] :
                 (N1954)? valid[193] :
                 (N1956)? valid[194] :
                 (N1958)? valid[195] :
                 (N1960)? valid[196] :
                 (N1962)? valid[197] :
                 (N1964)? valid[198] :
                 (N1966)? valid[199] :
                 (N1968)? valid[200] :
                 (N1970)? valid[201] :
                 (N1972)? valid[202] :
                 (N1974)? valid[203] :
                 (N1976)? valid[204] :
                 (N1978)? valid[205] :
                 (N1980)? valid[206] :
                 (N1982)? valid[207] :
                 (N1984)? valid[208] :
                 (N1986)? valid[209] :
                 (N1988)? valid[210] :
                 (N1990)? valid[211] :
                 (N1992)? valid[212] :
                 (N1994)? valid[213] :
                 (N1996)? valid[214] :
                 (N1998)? valid[215] :
                 (N2000)? valid[216] :
                 (N2002)? valid[217] :
                 (N2004)? valid[218] :
                 (N2006)? valid[219] :
                 (N2008)? valid[220] :
                 (N2010)? valid[221] :
                 (N2012)? valid[222] :
                 (N2014)? valid[223] :
                 (N2016)? valid[224] :
                 (N2018)? valid[225] :
                 (N2020)? valid[226] :
                 (N2022)? valid[227] :
                 (N2024)? valid[228] :
                 (N2026)? valid[229] :
                 (N2028)? valid[230] :
                 (N2030)? valid[231] :
                 (N2032)? valid[232] :
                 (N2034)? valid[233] :
                 (N2036)? valid[234] :
                 (N2038)? valid[235] :
                 (N2040)? valid[236] :
                 (N2042)? valid[237] :
                 (N2044)? valid[238] :
                 (N2046)? valid[239] :
                 (N2048)? valid[240] :
                 (N2050)? valid[241] :
                 (N2052)? valid[242] :
                 (N2054)? valid[243] :
                 (N2056)? valid[244] :
                 (N2058)? valid[245] :
                 (N2060)? valid[246] :
                 (N2062)? valid[247] :
                 (N2064)? valid[248] :
                 (N2066)? valid[249] :
                 (N2068)? valid[250] :
                 (N2070)? valid[251] :
                 (N2072)? valid[252] :
                 (N2074)? valid[253] :
                 (N2076)? valid[254] :
                 (N2078)? valid[255] :
                 (N1569)? valid[256] :
                 (N1571)? valid[257] :
                 (N1573)? valid[258] :
                 (N1575)? valid[259] :
                 (N1577)? valid[260] :
                 (N1579)? valid[261] :
                 (N1581)? valid[262] :
                 (N1583)? valid[263] :
                 (N1585)? valid[264] :
                 (N1587)? valid[265] :
                 (N1589)? valid[266] :
                 (N1591)? valid[267] :
                 (N1593)? valid[268] :
                 (N1595)? valid[269] :
                 (N1597)? valid[270] :
                 (N1599)? valid[271] :
                 (N1601)? valid[272] :
                 (N1603)? valid[273] :
                 (N1605)? valid[274] :
                 (N1607)? valid[275] :
                 (N1609)? valid[276] :
                 (N1611)? valid[277] :
                 (N1613)? valid[278] :
                 (N1615)? valid[279] :
                 (N1617)? valid[280] :
                 (N1619)? valid[281] :
                 (N1621)? valid[282] :
                 (N1623)? valid[283] :
                 (N1625)? valid[284] :
                 (N1627)? valid[285] :
                 (N1629)? valid[286] :
                 (N1631)? valid[287] :
                 (N1633)? valid[288] :
                 (N1635)? valid[289] :
                 (N1637)? valid[290] :
                 (N1639)? valid[291] :
                 (N1641)? valid[292] :
                 (N1643)? valid[293] :
                 (N1645)? valid[294] :
                 (N1647)? valid[295] :
                 (N1649)? valid[296] :
                 (N1651)? valid[297] :
                 (N1653)? valid[298] :
                 (N1655)? valid[299] :
                 (N1657)? valid[300] :
                 (N1659)? valid[301] :
                 (N1661)? valid[302] :
                 (N1663)? valid[303] :
                 (N1665)? valid[304] :
                 (N1667)? valid[305] :
                 (N1669)? valid[306] :
                 (N1671)? valid[307] :
                 (N1673)? valid[308] :
                 (N1675)? valid[309] :
                 (N1677)? valid[310] :
                 (N1679)? valid[311] :
                 (N1681)? valid[312] :
                 (N1683)? valid[313] :
                 (N1685)? valid[314] :
                 (N1687)? valid[315] :
                 (N1689)? valid[316] :
                 (N1691)? valid[317] :
                 (N1693)? valid[318] :
                 (N1695)? valid[319] :
                 (N1697)? valid[320] :
                 (N1699)? valid[321] :
                 (N1701)? valid[322] :
                 (N1703)? valid[323] :
                 (N1705)? valid[324] :
                 (N1707)? valid[325] :
                 (N1709)? valid[326] :
                 (N1711)? valid[327] :
                 (N1713)? valid[328] :
                 (N1715)? valid[329] :
                 (N1717)? valid[330] :
                 (N1719)? valid[331] :
                 (N1721)? valid[332] :
                 (N1723)? valid[333] :
                 (N1725)? valid[334] :
                 (N1727)? valid[335] :
                 (N1729)? valid[336] :
                 (N1731)? valid[337] :
                 (N1733)? valid[338] :
                 (N1735)? valid[339] :
                 (N1737)? valid[340] :
                 (N1739)? valid[341] :
                 (N1741)? valid[342] :
                 (N1743)? valid[343] :
                 (N1745)? valid[344] :
                 (N1747)? valid[345] :
                 (N1749)? valid[346] :
                 (N1751)? valid[347] :
                 (N1753)? valid[348] :
                 (N1755)? valid[349] :
                 (N1757)? valid[350] :
                 (N1759)? valid[351] :
                 (N1761)? valid[352] :
                 (N1763)? valid[353] :
                 (N1765)? valid[354] :
                 (N1767)? valid[355] :
                 (N1769)? valid[356] :
                 (N1771)? valid[357] :
                 (N1773)? valid[358] :
                 (N1775)? valid[359] :
                 (N1777)? valid[360] :
                 (N1779)? valid[361] :
                 (N1781)? valid[362] :
                 (N1783)? valid[363] :
                 (N1785)? valid[364] :
                 (N1787)? valid[365] :
                 (N1789)? valid[366] :
                 (N1791)? valid[367] :
                 (N1793)? valid[368] :
                 (N1795)? valid[369] :
                 (N1797)? valid[370] :
                 (N1799)? valid[371] :
                 (N1801)? valid[372] :
                 (N1803)? valid[373] :
                 (N1805)? valid[374] :
                 (N1807)? valid[375] :
                 (N1809)? valid[376] :
                 (N1811)? valid[377] :
                 (N1813)? valid[378] :
                 (N1815)? valid[379] :
                 (N1817)? valid[380] :
                 (N1819)? valid[381] :
                 (N1821)? valid[382] :
                 (N1823)? valid[383] :
                 (N1825)? valid[384] :
                 (N1827)? valid[385] :
                 (N1829)? valid[386] :
                 (N1831)? valid[387] :
                 (N1833)? valid[388] :
                 (N1835)? valid[389] :
                 (N1837)? valid[390] :
                 (N1839)? valid[391] :
                 (N1841)? valid[392] :
                 (N1843)? valid[393] :
                 (N1845)? valid[394] :
                 (N1847)? valid[395] :
                 (N1849)? valid[396] :
                 (N1851)? valid[397] :
                 (N1853)? valid[398] :
                 (N1855)? valid[399] :
                 (N1857)? valid[400] :
                 (N1859)? valid[401] :
                 (N1861)? valid[402] :
                 (N1863)? valid[403] :
                 (N1865)? valid[404] :
                 (N1867)? valid[405] :
                 (N1869)? valid[406] :
                 (N1871)? valid[407] :
                 (N1873)? valid[408] :
                 (N1875)? valid[409] :
                 (N1877)? valid[410] :
                 (N1879)? valid[411] :
                 (N1881)? valid[412] :
                 (N1883)? valid[413] :
                 (N1885)? valid[414] :
                 (N1887)? valid[415] :
                 (N1889)? valid[416] :
                 (N1891)? valid[417] :
                 (N1893)? valid[418] :
                 (N1895)? valid[419] :
                 (N1897)? valid[420] :
                 (N1899)? valid[421] :
                 (N1901)? valid[422] :
                 (N1903)? valid[423] :
                 (N1905)? valid[424] :
                 (N1907)? valid[425] :
                 (N1909)? valid[426] :
                 (N1911)? valid[427] :
                 (N1913)? valid[428] :
                 (N1915)? valid[429] :
                 (N1917)? valid[430] :
                 (N1919)? valid[431] :
                 (N1921)? valid[432] :
                 (N1923)? valid[433] :
                 (N1925)? valid[434] :
                 (N1927)? valid[435] :
                 (N1929)? valid[436] :
                 (N1931)? valid[437] :
                 (N1933)? valid[438] :
                 (N1935)? valid[439] :
                 (N1937)? valid[440] :
                 (N1939)? valid[441] :
                 (N1941)? valid[442] :
                 (N1943)? valid[443] :
                 (N1945)? valid[444] :
                 (N1947)? valid[445] :
                 (N1949)? valid[446] :
                 (N1951)? valid[447] :
                 (N1953)? valid[448] :
                 (N1955)? valid[449] :
                 (N1957)? valid[450] :
                 (N1959)? valid[451] :
                 (N1961)? valid[452] :
                 (N1963)? valid[453] :
                 (N1965)? valid[454] :
                 (N1967)? valid[455] :
                 (N1969)? valid[456] :
                 (N1971)? valid[457] :
                 (N1973)? valid[458] :
                 (N1975)? valid[459] :
                 (N1977)? valid[460] :
                 (N1979)? valid[461] :
                 (N1981)? valid[462] :
                 (N1983)? valid[463] :
                 (N1985)? valid[464] :
                 (N1987)? valid[465] :
                 (N1989)? valid[466] :
                 (N1991)? valid[467] :
                 (N1993)? valid[468] :
                 (N1995)? valid[469] :
                 (N1997)? valid[470] :
                 (N1999)? valid[471] :
                 (N2001)? valid[472] :
                 (N2003)? valid[473] :
                 (N2005)? valid[474] :
                 (N2007)? valid[475] :
                 (N2009)? valid[476] :
                 (N2011)? valid[477] :
                 (N2013)? valid[478] :
                 (N2015)? valid[479] :
                 (N2017)? valid[480] :
                 (N2019)? valid[481] :
                 (N2021)? valid[482] :
                 (N2023)? valid[483] :
                 (N2025)? valid[484] :
                 (N2027)? valid[485] :
                 (N2029)? valid[486] :
                 (N2031)? valid[487] :
                 (N2033)? valid[488] :
                 (N2035)? valid[489] :
                 (N2037)? valid[490] :
                 (N2039)? valid[491] :
                 (N2041)? valid[492] :
                 (N2043)? valid[493] :
                 (N2045)? valid[494] :
                 (N2047)? valid[495] :
                 (N2049)? valid[496] :
                 (N2051)? valid[497] :
                 (N2053)? valid[498] :
                 (N2055)? valid[499] :
                 (N2057)? valid[500] :
                 (N2059)? valid[501] :
                 (N2061)? valid[502] :
                 (N2063)? valid[503] :
                 (N2065)? valid[504] :
                 (N2067)? valid[505] :
                 (N2069)? valid[506] :
                 (N2071)? valid[507] :
                 (N2073)? valid[508] :
                 (N2075)? valid[509] :
                 (N2077)? valid[510] :
                 (N2079)? valid[511] :"""

    p = re.compile(r'^\s*\((.+)\).*valid\[(\d+)\].*$')

    a = []
    for line in txt.split('\n'):
        line = line.rstrip('\n')

        m = p.match(line)
        assert m is not None

        a.append(m.groups())

    assert all( idx == int(idx_s) for idx, (_, idx_s) in enumerate(a))

    ss = ', '.join(sig for sig, idx in reversed(a))
        
    print(f'   alt_priority_mux_512 my_priority_mux(.s({{ {ss} }}), .d(valid), .dd(N2080));')


if __name__ == "__main__":
    main()
    driver()
