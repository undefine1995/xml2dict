# coding:utf-8
import xml2dict
from xml.etree import ElementTree as ET
e = ET.XML('''
<list>
<node id="shpd-app142" claimed="true" class="system" handle="DMI:0024">
 <description>Rack Mount Chassis</description>
 <product>System x3650 M4 : -[7915R01]- ()</product>
 <vendor>IBM</vendor>
 <version>0C</version>
 <serial>06ZZYK6</serial>
 <width units="bits">64</width>
 <configuration>
  <setting id="boot" value="normal" />
  <setting id="chassis" value="rackmount" />
  <setting id="family" value="System X" />
  <setting id="uuid" value="8AB72180-129D-E311-9A6A-40F2E998F542" />
 </configuration>
 <capabilities>
  <capability id="smbios-2.7" >SMBIOS version 2.7</capability>
  <capability id="dmi-2.7" >DMI version 2.7</capability>
  <capability id="vsyscall64" >64-bit processes</capability>
  <capability id="vsyscall32" >32-bit processes</capability>
 </capabilities>
  <node id="core" claimed="true" class="bus" handle="DMI:0025">
   <description>Motherboard</description>
   <product>00Y8473</product>
   <vendor>IBM</vendor>
   <physid>0</physid>
   <serial>42306J</serial>
   <slot>Blade</slot>
    <node id="cpu:0" claimed="true" class="processor" handle="DMI:0001">
     <description>CPU</description>
     <product>Intel(R) Xeon(R) CPU E5-2603 v2 @ 1.80GHz</product>
     <vendor>Intel Corp.</vendor>
     <physid>1</physid>
     <businfo>cpu@0</businfo>
     <version>Intel(R) Xeon(R) CPU E5-2603 v2 @ 1.80GHz</version>
     <slot>Socket 1</slot>
     <size units="Hz">1200000000</size>
     <capacity units="Hz">4000000000</capacity>
     <width units="bits">64</width>
     <clock units="Hz">100000000</clock>
     <configuration>
      <setting id="cores" value="4" />
      <setting id="enabledcores" value="4" />
      <setting id="threads" value="4" />
     </configuration>
     <capabilities>
      <capability id="x86-64" >64bits extensions (x86-64)</capability>
      <capability id="fpu" >mathematical co-processor</capability>
      <capability id="fpu_exception" >FPU exceptions reporting</capability>
      <capability id="wp" />
      <capability id="vme" >virtual mode extensions</capability>
      <capability id="de" >debugging extensions</capability>
      <capability id="pse" >page size extensions</capability>
      <capability id="tsc" >time stamp counter</capability>
      <capability id="msr" >model-specific registers</capability>
      <capability id="pae" >4GB+ memory addressing (Physical Address Extension)</capability>
      <capability id="mce" >machine check exceptions</capability>
      <capability id="cx8" >compare and exchange 8-byte</capability>
      <capability id="apic" >on-chip advanced programmable interrupt controller (APIC)</capability>
      <capability id="mtrr" >memory type range registers</capability>
      <capability id="pge" >page global enable</capability>
      <capability id="mca" >machine check architecture</capability>
      <capability id="cmov" >conditional move instruction</capability>
      <capability id="pat" >page attribute table</capability>
      <capability id="pse36" >36-bit page size extensions</capability>
      <capability id="clflush" />
      <capability id="dts" >debug trace and EMON store MSRs</capability>
      <capability id="acpi" >thermal control (ACPI)</capability>
      <capability id="mmx" >multimedia extensions (MMX)</capability>
      <capability id="fxsr" >fast floating point save/restore</capability>
      <capability id="sse" >streaming SIMD extensions (SSE)</capability>
      <capability id="sse2" >streaming SIMD extensions (SSE2)</capability>
      <capability id="ss" >self-snoop</capability>
      <capability id="ht" >HyperThreading</capability>
      <capability id="tm" >thermal interrupt and status</capability>
      <capability id="pbe" >pending break event</capability>
      <capability id="syscall" >fast system calls</capability>
      <capability id="nx" >no-execute bit (NX)</capability>
      <capability id="pdpe1gb" />
      <capability id="rdtscp" />
      <capability id="constant_tsc" />
      <capability id="arch_perfmon" />
      <capability id="pebs" />
      <capability id="bts" />
      <capability id="rep_good" />
      <capability id="xtopology" />
      <capability id="nonstop_tsc" />
      <capability id="aperfmperf" />
      <capability id="pni" />
      <capability id="pclmulqdq" />
      <capability id="dtes64" />
      <capability id="monitor" />
      <capability id="ds_cpl" />
      <capability id="vmx" />
      <capability id="smx" />
      <capability id="est" />
      <capability id="tm2" />
      <capability id="ssse3" />
      <capability id="cx16" />
      <capability id="xtpr" />
      <capability id="pdcm" />
      <capability id="dca" />
      <capability id="sse4_1" />
      <capability id="sse4_2" />
      <capability id="x2apic" />
      <capability id="popcnt" />
      <capability id="aes" />
      <capability id="xsave" />
      <capability id="avx" />
      <capability id="f16c" />
      <capability id="rdrand" />
      <capability id="lahf_lm" />
      <capability id="arat" />
      <capability id="epb" />
      <capability id="xsaveopt" />
      <capability id="pln" />
      <capability id="pts" />
      <capability id="tpr_shadow" />
      <capability id="vnmi" />
      <capability id="flexpriority" />
      <capability id="ept" />
      <capability id="vpid" />
      <capability id="fsgsbase" />
      <capability id="smep" />
      <capability id="erms" />
      <capability id="cpufreq" >CPU Frequency scaling</capability>
     </capabilities>
      <node id="cache:0" claimed="true" class="memory" handle="DMI:0003">
       <description>L1 cache</description>
       <physid>3</physid>
       <slot>Internal Cache Level 1</slot>
       <size units="bytes">65536</size>
       <capacity units="bytes">65536</capacity>
       <capabilities>
        <capability id="asynchronous" >Asynchronous</capability>
        <capability id="internal" >Internal</capability>
        <capability id="write-back" >Write-back</capability>
        <capability id="instruction" >Instruction cache</capability>
       </capabilities>
      </node>
      <node id="cache:1" claimed="true" class="memory" handle="DMI:0004">
       <description>L2 cache</description>
       <physid>4</physid>
       <slot>Internal Cache Level 2</slot>
       <size units="bytes">262144</size>
       <capacity units="bytes">262144</capacity>
       <capabilities>
        <capability id="asynchronous" >Asynchronous</capability>
        <capability id="internal" >Internal</capability>
        <capability id="write-back" >Write-back</capability>
        <capability id="unified" >Unified cache</capability>
       </capabilities>
      </node>
      <node id="cache:2" claimed="true" class="memory" handle="DMI:0005">
       <description>L3 cache</description>
       <physid>5</physid>
       <slot>Internal Cache Level 3</slot>
       <size units="bytes">10485760</size>
       <capacity units="bytes">10485760</capacity>
       <capabilities>
        <capability id="asynchronous" >Asynchronous</capability>
        <capability id="internal" >Internal</capability>
        <capability id="write-back" >Write-back</capability>
        <capability id="unified" >Unified cache</capability>
       </capabilities>
      </node>
    </node>
    <node id="cpu:1" claimed="true" class="processor" handle="DMI:0002">
     <description>CPU</description>
     <product>Intel(R) Xeon(R) CPU E5-2603 v2 @ 1.80GHz</product>
     <vendor>Intel Corp.</vendor>
     <physid>2</physid>
     <businfo>cpu@1</businfo>
     <version>Intel(R) Xeon(R) CPU E5-2603 v2 @ 1.80GHz</version>
     <slot>Socket 2</slot>
     <size units="Hz">1800000000</size>
     <capacity units="Hz">4000000000</capacity>
     <width units="bits">64</width>
     <clock units="Hz">100000000</clock>
     <configuration>
      <setting id="cores" value="4" />
      <setting id="enabledcores" value="4" />
      <setting id="threads" value="4" />
     </configuration>
     <capabilities>
      <capability id="x86-64" >64bits extensions (x86-64)</capability>
      <capability id="fpu" >mathematical co-processor</capability>
      <capability id="fpu_exception" >FPU exceptions reporting</capability>
      <capability id="wp" />
      <capability id="vme" >virtual mode extensions</capability>
      <capability id="de" >debugging extensions</capability>
      <capability id="pse" >page size extensions</capability>
      <capability id="tsc" >time stamp counter</capability>
      <capability id="msr" >model-specific registers</capability>
      <capability id="pae" >4GB+ memory addressing (Physical Address Extension)</capability>
      <capability id="mce" >machine check exceptions</capability>
      <capability id="cx8" >compare and exchange 8-byte</capability>
      <capability id="apic" >on-chip advanced programmable interrupt controller (APIC)</capability>
      <capability id="mtrr" >memory type range registers</capability>
      <capability id="pge" >page global enable</capability>
      <capability id="mca" >machine check architecture</capability>
      <capability id="cmov" >conditional move instruction</capability>
      <capability id="pat" >page attribute table</capability>
      <capability id="pse36" >36-bit page size extensions</capability>
      <capability id="clflush" />
      <capability id="dts" >debug trace and EMON store MSRs</capability>
      <capability id="acpi" >thermal control (ACPI)</capability>
      <capability id="mmx" >multimedia extensions (MMX)</capability>
      <capability id="fxsr" >fast floating point save/restore</capability>
      <capability id="sse" >streaming SIMD extensions (SSE)</capability>
      <capability id="sse2" >streaming SIMD extensions (SSE2)</capability>
      <capability id="ss" >self-snoop</capability>
      <capability id="ht" >HyperThreading</capability>
      <capability id="tm" >thermal interrupt and status</capability>
      <capability id="pbe" >pending break event</capability>
      <capability id="syscall" >fast system calls</capability>
      <capability id="nx" >no-execute bit (NX)</capability>
      <capability id="pdpe1gb" />
      <capability id="rdtscp" />
      <capability id="constant_tsc" />
      <capability id="arch_perfmon" />
      <capability id="pebs" />
      <capability id="bts" />
      <capability id="rep_good" />
      <capability id="xtopology" />
      <capability id="nonstop_tsc" />
      <capability id="aperfmperf" />
      <capability id="pni" />
      <capability id="pclmulqdq" />
      <capability id="dtes64" />
      <capability id="monitor" />
      <capability id="ds_cpl" />
      <capability id="vmx" />
      <capability id="smx" />
      <capability id="est" />
      <capability id="tm2" />
      <capability id="ssse3" />
      <capability id="cx16" />
      <capability id="xtpr" />
      <capability id="pdcm" />
      <capability id="dca" />
      <capability id="sse4_1" />
      <capability id="sse4_2" />
      <capability id="x2apic" />
      <capability id="popcnt" />
      <capability id="aes" />
      <capability id="xsave" />
      <capability id="avx" />
      <capability id="f16c" />
      <capability id="rdrand" />
      <capability id="lahf_lm" />
      <capability id="arat" />
      <capability id="epb" />
      <capability id="xsaveopt" />
      <capability id="pln" />
      <capability id="pts" />
      <capability id="tpr_shadow" />
      <capability id="vnmi" />
      <capability id="flexpriority" />
      <capability id="ept" />
      <capability id="vpid" />
      <capability id="fsgsbase" />
      <capability id="smep" />
      <capability id="erms" />
      <capability id="cpufreq" >CPU Frequency scaling</capability>
     </capabilities>
      <node id="cache:0" claimed="true" class="memory" handle="DMI:0006">
       <description>L1 cache</description>
       <physid>6</physid>
       <slot>Internal Cache Level 1</slot>
       <size units="bytes">65536</size>
       <capacity units="bytes">65536</capacity>
       <capabilities>
        <capability id="asynchronous" >Asynchronous</capability>
        <capability id="internal" >Internal</capability>
        <capability id="write-back" >Write-back</capability>
        <capability id="instruction" >Instruction cache</capability>
       </capabilities>
      </node>
      <node id="cache:1" claimed="true" class="memory" handle="DMI:0007">
       <description>L2 cache</description>
       <physid>7</physid>
       <slot>Internal Cache Level 2</slot>
       <size units="bytes">262144</size>
       <capacity units="bytes">262144</capacity>
       <capabilities>
        <capability id="asynchronous" >Asynchronous</capability>
        <capability id="internal" >Internal</capability>
        <capability id="write-back" >Write-back</capability>
        <capability id="unified" >Unified cache</capability>
       </capabilities>
      </node>
      <node id="cache:2" claimed="true" class="memory" handle="DMI:0008">
       <description>L3 cache</description>
       <physid>8</physid>
       <slot>Internal Cache Level 3</slot>
       <size units="bytes">10485760</size>
       <capacity units="bytes">10485760</capacity>
       <capabilities>
        <capability id="asynchronous" >Asynchronous</capability>
        <capability id="internal" >Internal</capability>
        <capability id="write-back" >Write-back</capability>
        <capability id="unified" >Unified cache</capability>
       </capabilities>
      </node>
    </node>
    <node id="memory" claimed="true" class="memory" handle="DMI:0009">
     <description>System Memory</description>
     <physid>9</physid>
     <slot>System board or motherboard</slot>
     <size units="bytes">8589934592</size>
      <node id="bank:0" claimed="true" class="memory" handle="DMI:000A">
       <description>DIMM DDR3 1600 MHz (0.6 ns)</description>
       <product>M393B5270DH0-YK0</product>
       <vendor>Samsung</vendor>
       <physid>0</physid>
       <serial>3338070D</serial>
       <slot>DIMM 1</slot>
       <size units="bytes">4294967296</size>
       <width units="bits">64</width>
       <clock units="Hz">1600000000</clock>
      </node>
      <node id="bank:1" claimed="true" class="memory" handle="DMI:000B">
       <description>[empty]</description>
       <physid>1</physid>
       <slot>DIMM 2</slot>
      </node>
      <node id="bank:2" claimed="true" class="memory" handle="DMI:000C">
       <description>[empty]</description>
       <physid>2</physid>
       <slot>DIMM 3</slot>
      </node>
      <node id="bank:3" claimed="true" class="memory" handle="DMI:000D">
       <description>[empty]</description>
       <physid>3</physid>
       <slot>DIMM 4</slot>
      </node>
      <node id="bank:4" claimed="true" class="memory" handle="DMI:000E">
       <description>[empty]</description>
       <physid>4</physid>
       <slot>DIMM 5</slot>
      </node>
      <node id="bank:5" claimed="true" class="memory" handle="DMI:000F">
       <description>[empty]</description>
       <physid>5</physid>
       <slot>DIMM 6</slot>
      </node>
      <node id="bank:6" claimed="true" class="memory" handle="DMI:0010">
       <description>[empty]</description>
       <physid>6</physid>
       <slot>DIMM 7</slot>
      </node>
      <node id="bank:7" claimed="true" class="memory" handle="DMI:0011">
       <description>[empty]</description>
       <physid>7</physid>
       <slot>DIMM 8</slot>
      </node>
      <node id="bank:8" claimed="true" class="memory" handle="DMI:0012">
       <description>[empty]</description>
       <physid>8</physid>
       <slot>DIMM 9</slot>
      </node>
      <node id="bank:9" claimed="true" class="memory" handle="DMI:0013">
       <description>[empty]</description>
       <physid>9</physid>
       <slot>DIMM 10</slot>
      </node>
      <node id="bank:10" claimed="true" class="memory" handle="DMI:0014">
       <description>[empty]</description>
       <physid>a</physid>
       <slot>DIMM 11</slot>
      </node>
      <node id="bank:11" claimed="true" class="memory" handle="DMI:0015">
       <description>[empty]</description>
       <physid>b</physid>
       <slot>DIMM 12</slot>
      </node>
      <node id="bank:12" claimed="true" class="memory" handle="DMI:0016">
       <description>DIMM DDR3 1600 MHz (0.6 ns)</description>
       <product>M393B5270DH0-YK0</product>
       <vendor>Samsung</vendor>
       <physid>c</physid>
       <serial>3338070D</serial>
       <slot>DIMM 13</slot>
       <size units="bytes">4294967296</size>
       <width units="bits">64</width>
       <clock units="Hz">1600000000</clock>
      </node>
      <node id="bank:13" claimed="true" class="memory" handle="DMI:0017">
       <description>[empty]</description>
       <physid>d</physid>
       <slot>DIMM 14</slot>
      </node>
      <node id="bank:14" claimed="true" class="memory" handle="DMI:0018">
       <description>[empty]</description>
       <physid>e</physid>
       <slot>DIMM 15</slot>
      </node>
      <node id="bank:15" claimed="true" class="memory" handle="DMI:0019">
       <description>[empty]</description>
       <physid>f</physid>
       <slot>DIMM 16</slot>
      </node>
      <node id="bank:16" claimed="true" class="memory" handle="DMI:001A">
       <description>[empty]</description>
       <physid>10</physid>
       <serial>Bank 1</serial>
       <slot>DIMM 17</slot>
      </node>
      <node id="bank:17" claimed="true" class="memory" handle="DMI:001B">
       <description>[empty]</description>
       <physid>11</physid>
       <serial>Bank 2</serial>
       <slot>DIMM 18</slot>
      </node>
      <node id="bank:18" claimed="true" class="memory" handle="DMI:001C">
       <description>[empty]</description>
       <physid>12</physid>
       <serial>Bank 3</serial>
       <slot>DIMM 19</slot>
      </node>
      <node id="bank:19" claimed="true" class="memory" handle="DMI:001D">
       <description>[empty]</description>
       <physid>13</physid>
       <serial>Bank 4</serial>
       <slot>DIMM 20</slot>
      </node>
      <node id="bank:20" claimed="true" class="memory" handle="DMI:001E">
       <description>[empty]</description>
       <physid>14</physid>
       <serial>Bank 5</serial>
       <slot>DIMM 21</slot>
      </node>
      <node id="bank:21" claimed="true" class="memory" handle="DMI:001F">
       <description>[empty]</description>
       <physid>15</physid>
       <serial>Bank 6</serial>
       <slot>DIMM 22</slot>
      </node>
      <node id="bank:22" claimed="true" class="memory" handle="DMI:0020">
       <description>[empty]</description>
       <physid>16</physid>
       <serial>Bank 7</serial>
       <slot>DIMM 23</slot>
      </node>
      <node id="bank:23" claimed="true" class="memory" handle="DMI:0021">
       <description>[empty]</description>
       <physid>17</physid>
       <serial>Bank 8</serial>
       <slot>DIMM 24</slot>
      </node>
    </node>
    <node id="firmware" claimed="true" class="memory" handle="">
     <description>BIOS</description>
     <vendor>IBM</vendor>
     <physid>23</physid>
     <version>-[VVE136AUS-1.60]-</version>
     <date>12/12/2013</date>
     <size units="bytes">131072</size>
     <capacity units="bytes">8323072</capacity>
     <capabilities>
      <capability id="pci" >PCI bus</capability>
      <capability id="pnp" >Plug-and-Play</capability>
      <capability id="upgrade" >BIOS EEPROM can be upgraded</capability>
      <capability id="shadowing" >BIOS shadowing</capability>
      <capability id="cdboot" >Booting from CD-ROM/DVD</capability>
      <capability id="bootselect" >Selectable boot path</capability>
      <capability id="edd" >Enhanced Disk Drive extensions</capability>
      <capability id="int5printscreen" >Print Screen key</capability>
      <capability id="int9keyboard" >i8042 keyboard controller</capability>
      <capability id="int14serial" >INT14 serial line control</capability>
      <capability id="int10video" >INT10 CGA/Mono video</capability>
      <capability id="acpi" >ACPI</capability>
      <capability id="usb" >USB legacy emulation</capability>
      <capability id="netboot" >Function-key initiated network service boot</capability>
     </capabilities>
    </node>
    <node id="pci:0" claimed="true" class="bridge" handle="PCIBUS:0000:00">
     <description>Host bridge</description>
     <product>Intel Corporation [8086:E00]</product>
     <vendor>Intel Corporation [8086]</vendor>
     <physid>100</physid>
     <businfo>pci@0000:00:00.0</businfo>
     <version>04</version>
     <width units="bits">32</width>
     <clock units="Hz">33000000</clock>
      <node id="pci:0" claimed="true" class="bridge" handle="PCIBUS:0000:0c">
       <description>PCI bridge</description>
       <product>Intel Corporation [8086:E02]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>1</physid>
       <businfo>pci@0000:00:01.0</businfo>
       <version>04</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="pcieport" />
       </configuration>
       <capabilities>
        <capability id="pci" />
        <capability id="msi" >Message Signalled Interrupts</capability>
        <capability id="pciexpress" >PCI Express</capability>
        <capability id="pm" >Power Management</capability>
        <capability id="normal_decode" />
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="irq" value="79" />
       </resources>
      </node>
      <node id="pci:1" claimed="true" class="bridge" handle="PCIBUS:0000:11">
       <description>PCI bridge</description>
       <product>Intel Corporation [8086:E04]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>2</physid>
       <businfo>pci@0000:00:02.0</businfo>
       <version>04</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="pcieport" />
       </configuration>
       <capabilities>
        <capability id="pci" />
        <capability id="msi" >Message Signalled Interrupts</capability>
        <capability id="pciexpress" >PCI Express</capability>
        <capability id="pm" >Power Management</capability>
        <capability id="normal_decode" />
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="irq" value="80" />
       </resources>
      </node>
      <node id="pci:2" claimed="true" class="bridge" handle="PCIBUS:0000:16">
       <description>PCI bridge</description>
       <product>Intel Corporation [8086:E06]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>2.2</physid>
       <businfo>pci@0000:00:02.2</businfo>
       <version>04</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="pcieport" />
       </configuration>
       <capabilities>
        <capability id="pci" />
        <capability id="msi" >Message Signalled Interrupts</capability>
        <capability id="pciexpress" >PCI Express</capability>
        <capability id="pm" >Power Management</capability>
        <capability id="normal_decode" />
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="irq" value="81" />
        <resource type="ioport" value="2000(size=4096)" />
        <resource type="memory" value="c4400000-c44fffff" />
        <resource type="memory" value="90100000-901fffff(prefetchable)" />
       </resources>
        <node id="storage" claimed="true" class="storage" handle="PCI:0000:16:00.0">
         <description>RAID bus controller</description>
         <product>MegaRAID SAS 2208 [Thunderbolt] [1000:5B]</product>
         <vendor>LSI Logic / Symbios Logic [1000]</vendor>
         <physid>0</physid>
         <businfo>pci@0000:16:00.0</businfo>
         <logicalname>scsi0</logicalname>
         <version>05</version>
         <width units="bits">64</width>
         <clock units="Hz">33000000</clock>
         <configuration>
          <setting id="driver" value="megaraid_sas" />
          <setting id="latency" value="0" />
         </configuration>
         <capabilities>
          <capability id="storage" />
          <capability id="pm" >Power Management</capability>
          <capability id="pciexpress" >PCI Express</capability>
          <capability id="vpd" >Vital Product Data</capability>
          <capability id="msi" >Message Signalled Interrupts</capability>
          <capability id="msix" >MSI-X</capability>
          <capability id="bus_master" >bus mastering</capability>
          <capability id="cap_list" >PCI capabilities listing</capability>
          <capability id="rom" >extension ROM</capability>
         </capabilities>
         <resources>
          <resource type="irq" value="34" />
          <resource type="ioport" value="2f00(size=256)" />
          <resource type="memory" value="c44bc000-c44bffff" />
          <resource type="memory" value="c44c0000-c44fffff" />
          <resource type="memory" value="90100000-9011ffff(prefetchable)" />
         </resources>
          <node id="disk" claimed="true" class="disk" handle="SCSI:00:02:00:00">
           <description>SCSI Disk</description>
           <product>ServeRAID M5110e</product>
           <vendor>IBM</vendor>
           <physid>2.0.0</physid>
           <businfo>scsi@0:2.0.0</businfo>
           <logicalname>/dev/sda</logicalname>
           <dev>8:0</dev>
           <version>3.27</version>
           <serial>00670b67097dcad11a40f51158600705</serial>
           <size units="bytes">597998698496</size>
           <configuration>
            <setting id="ansiversion" value="5" />
            <setting id="sectorsize" value="4096" />
            <setting id="signature" value="000c94eb" />
           </configuration>
           <capabilities>
            <capability id="partitioned" >Partitioned disk</capability>
            <capability id="partitioned:dos" >MS-DOS partition table</capability>
           </capabilities>
            <node id="volume:0" claimed="true" class="volume" handle="">
             <description>Windows FAT volume</description>
             <vendor>mkdosfs</vendor>
             <physid>1</physid>
             <businfo>scsi@0:2.0.0,1</businfo>
             <logicalname>/dev/sda1</logicalname>
             <logicalname>/boot/efi</logicalname>
             <dev>8:1</dev>
             <version>FAT16</version>
             <serial>fe51-b100</serial>
             <size units="bytes">524279808</size>
             <capacity>524288000</capacity>
             <configuration>
              <setting id="FATs" value="2" />
              <setting id="filesystem" value="fat" />
              <setting id="mount.fstype" value="vfat" />
              <setting id="mount.options" value="rw,relatime,fmask=0077,dmask=0077,codepage=cp437,iocharset=ascii,shortname=winnt,errors=remount-ro" />
              <setting id="state" value="mounted" />
             </configuration>
             <capabilities>
              <capability id="primary" >Primary partition</capability>
              <capability id="fat" >Windows FAT</capability>
              <capability id="initialized" >initialized volume</capability>
             </capabilities>
            </node>
            <node id="volume:1" claimed="true" class="volume" handle="">
             <description>EXT4 volume</description>
             <vendor>Linux</vendor>
             <physid>2</physid>
             <businfo>scsi@0:2.0.0,2</businfo>
             <logicalname>/dev/sda2</logicalname>
             <logicalname>/boot</logicalname>
             <dev>8:2</dev>
             <version>1.0</version>
             <serial>6855aadd-155f-4a4f-b2fb-05547f36de50</serial>
             <size units="bytes">209715200</size>
             <capacity>209715200</capacity>
             <configuration>
              <setting id="created" value="2014-04-21 23:57:25" />
              <setting id="filesystem" value="ext4" />
              <setting id="lastmountpoint" value="/boot" />
              <setting id="modified" value="2015-01-24 02:02:41" />
              <setting id="mount.fstype" value="ext4" />
              <setting id="mount.options" value="rw,seclabel,nosuid,nodev,noexec,relatime,barrier=1,data=ordered" />
              <setting id="mounted" value="2015-01-24 02:02:41" />
              <setting id="state" value="mounted" />
             </configuration>
             <capabilities>
              <capability id="primary" >Primary partition</capability>
              <capability id="bootable" >Bootable partition (active)</capability>
              <capability id="journaled" />
              <capability id="extended_attributes" >Extended Attributes</capability>
              <capability id="huge_files" >16TB+ files</capability>
              <capability id="dir_nlink" >directories with 65000+ subdirs</capability>
              <capability id="recover" >needs recovery</capability>
              <capability id="extents" >extent-based allocation</capability>
              <capability id="ext4" />
              <capability id="ext2" >EXT2/EXT3</capability>
              <capability id="initialized" >initialized volume</capability>
             </capabilities>
            </node>
            <node id="volume:2" claimed="true" class="volume" handle="">
             <description>Linux LVM Physical Volume partition</description>
             <physid>3</physid>
             <businfo>scsi@0:2.0.0,3</businfo>
             <logicalname>/dev/sda3</logicalname>
             <dev>8:3</dev>
             <serial>0H2JrE-zmmU-BRnl-FX26-tK3O-Ypdh-HfYtOC</serial>
             <size units="bytes">31457280000</size>
             <capacity>31457280000</capacity>
             <capabilities>
              <capability id="primary" >Primary partition</capability>
              <capability id="multi" >Multi-volumes</capability>
              <capability id="lvm2" />
             </capabilities>
            </node>
            <node id="volume:3" claimed="true" class="volume" handle="">
             <description>Extended partition</description>
             <physid>4</physid>
             <businfo>scsi@0:2.0.0,4</businfo>
             <logicalname>/dev/sda4</logicalname>
             <dev>8:4</dev>
             <size units="bytes">565806366720</size>
             <capacity>565806366720</capacity>
             <capabilities>
              <capability id="primary" >Primary partition</capability>
              <capability id="extended" >Extended partition</capability>
              <capability id="partitioned" >Partitioned disk</capability>
              <capability id="partitioned:extended" >Extended partition</capability>
             </capabilities>
              <node id="logicalvolume:0" claimed="true" class="volume" handle="">
               <description>Linux swap / Solaris partition</description>
               <physid>5</physid>
               <logicalname>/dev/sda5</logicalname>
               <dev>8:5</dev>
               <capacity>8589934592</capacity>
               <capabilities>
                <capability id="nofs" >No filesystem</capability>
               </capabilities>
              </node>
              <node id="logicalvolume:1" claimed="true" class="volume" handle="">
               <description>Linux LVM Physical Volume partition</description>
               <physid>6</physid>
               <logicalname>/dev/sda6</logicalname>
               <dev>8:6</dev>
               <serial>eQxDWy-WQMc-jfln-IGzQ-P9kA-dcE8-nw7K2O</serial>
               <size units="bytes">557214334976</size>
               <capacity>557214334976</capacity>
               <capabilities>
                <capability id="multi" >Multi-volumes</capability>
                <capability id="lvm2" />
               </capabilities>
              </node>
            </node>
          </node>
        </node>
      </node>
      <node id="pci:3" claimed="true" class="bridge" handle="PCIBUS:0000:1b">
       <description>PCI bridge</description>
       <product>Intel Corporation [8086:E08]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>3</physid>
       <businfo>pci@0000:00:03.0</businfo>
       <version>04</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="pcieport" />
       </configuration>
       <capabilities>
        <capability id="pci" />
        <capability id="msi" >Message Signalled Interrupts</capability>
        <capability id="pciexpress" >PCI Express</capability>
        <capability id="pm" >Power Management</capability>
        <capability id="normal_decode" />
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="irq" value="82" />
       </resources>
      </node>
      <node id="pci:4" claimed="true" class="bridge" handle="PCIBUS:0000:20">
       <description>PCI bridge</description>
       <product>Intel Corporation [8086:E0A]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>3.2</physid>
       <businfo>pci@0000:00:03.2</businfo>
       <version>04</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="pcieport" />
       </configuration>
       <capabilities>
        <capability id="pci" />
        <capability id="msi" >Message Signalled Interrupts</capability>
        <capability id="pciexpress" >PCI Express</capability>
        <capability id="pm" >Power Management</capability>
        <capability id="normal_decode" />
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="irq" value="83" />
       </resources>
      </node>
      <node id="generic:0" class="generic" handle="PCI:0000:00:04.0">
       <description>System peripheral</description>
       <product>Intel Corporation [8086:E20]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>4</physid>
       <businfo>pci@0000:00:04.0</businfo>
       <version>04</version>
       <width units="bits">64</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="msix" >MSI-X</capability>
        <capability id="pciexpress" >PCI Express</capability>
        <capability id="pm" >Power Management</capability>
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="memory" value="c40e0000-c40e3fff" />
       </resources>
      </node>
      <node id="generic:1" class="generic" handle="PCI:0000:00:04.1">
       <description>System peripheral</description>
       <product>Intel Corporation [8086:E21]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>4.1</physid>
       <businfo>pci@0000:00:04.1</businfo>
       <version>04</version>
       <width units="bits">64</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="msix" >MSI-X</capability>
        <capability id="pciexpress" >PCI Express</capability>
        <capability id="pm" >Power Management</capability>
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="memory" value="c40e4000-c40e7fff" />
       </resources>
      </node>
      <node id="generic:2" class="generic" handle="PCI:0000:00:04.2">
       <description>System peripheral</description>
       <product>Intel Corporation [8086:E22]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>4.2</physid>
       <businfo>pci@0000:00:04.2</businfo>
       <version>04</version>
       <width units="bits">64</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="msix" >MSI-X</capability>
        <capability id="pciexpress" >PCI Express</capability>
        <capability id="pm" >Power Management</capability>
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="memory" value="c40e8000-c40ebfff" />
       </resources>
      </node>
      <node id="generic:3" class="generic" handle="PCI:0000:00:04.3">
       <description>System peripheral</description>
       <product>Intel Corporation [8086:E23]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>4.3</physid>
       <businfo>pci@0000:00:04.3</businfo>
       <version>04</version>
       <width units="bits">64</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="msix" >MSI-X</capability>
        <capability id="pciexpress" >PCI Express</capability>
        <capability id="pm" >Power Management</capability>
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="memory" value="c40ec000-c40effff" />
       </resources>
      </node>
      <node id="generic:4" class="generic" handle="PCI:0000:00:04.4">
       <description>System peripheral</description>
       <product>Intel Corporation [8086:E24]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>4.4</physid>
       <businfo>pci@0000:00:04.4</businfo>
       <version>04</version>
       <width units="bits">64</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="msix" >MSI-X</capability>
        <capability id="pciexpress" >PCI Express</capability>
        <capability id="pm" >Power Management</capability>
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="memory" value="c40f0000-c40f3fff" />
       </resources>
      </node>
      <node id="generic:5" class="generic" handle="PCI:0000:00:04.5">
       <description>System peripheral</description>
       <product>Intel Corporation [8086:E25]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>4.5</physid>
       <businfo>pci@0000:00:04.5</businfo>
       <version>04</version>
       <width units="bits">64</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="msix" >MSI-X</capability>
        <capability id="pciexpress" >PCI Express</capability>
        <capability id="pm" >Power Management</capability>
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="memory" value="c40f4000-c40f7fff" />
       </resources>
      </node>
      <node id="generic:6" class="generic" handle="PCI:0000:00:04.6">
       <description>System peripheral</description>
       <product>Intel Corporation [8086:E26]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>4.6</physid>
       <businfo>pci@0000:00:04.6</businfo>
       <version>04</version>
       <width units="bits">64</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="msix" >MSI-X</capability>
        <capability id="pciexpress" >PCI Express</capability>
        <capability id="pm" >Power Management</capability>
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="memory" value="c40f8000-c40fbfff" />
       </resources>
      </node>
      <node id="generic:7" class="generic" handle="PCI:0000:00:04.7">
       <description>System peripheral</description>
       <product>Intel Corporation [8086:E27]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>4.7</physid>
       <businfo>pci@0000:00:04.7</businfo>
       <version>04</version>
       <width units="bits">64</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="msix" >MSI-X</capability>
        <capability id="pciexpress" >PCI Express</capability>
        <capability id="pm" >Power Management</capability>
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="memory" value="c40fc000-c40fffff" />
       </resources>
      </node>
      <node id="generic:8" class="generic" handle="PCI:0000:00:05.0">
       <description>System peripheral</description>
       <product>Intel Corporation [8086:E28]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>5</physid>
       <businfo>pci@0000:00:05.0</businfo>
       <version>04</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="pciexpress" >PCI Express</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
      </node>
      <node id="generic:9" class="generic" handle="PCI:0000:00:05.2">
       <description>System peripheral</description>
       <product>Intel Corporation [8086:E2A]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>5.2</physid>
       <businfo>pci@0000:00:05.2</businfo>
       <version>04</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="pciexpress" >PCI Express</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
      </node>
      <node id="pci:5" claimed="true" class="bridge" handle="PCIBUS:0000:25">
       <description>PCI bridge</description>
       <product>Patsburg PCI Express Virtual Root Port [8086:1D3E]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>11</physid>
       <businfo>pci@0000:00:11.0</businfo>
       <version>06</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="pcieport" />
       </configuration>
       <capabilities>
        <capability id="pci" />
        <capability id="pciexpress" >PCI Express</capability>
        <capability id="pm" >Power Management</capability>
        <capability id="msi" >Message Signalled Interrupts</capability>
        <capability id="normal_decode" />
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="irq" value="84" />
       </resources>
      </node>
      <node id="usb:0" claimed="true" class="bus" handle="PCI:0000:00:1a.0">
       <description>USB controller</description>
       <product>Patsburg USB2 Enhanced Host Controller #2 [8086:1D2D]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>1a</physid>
       <businfo>pci@0000:00:1a.0</businfo>
       <version>06</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="ehci_hcd" />
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="pm" >Power Management</capability>
        <capability id="debug" >Debug port</capability>
        <capability id="ehci" >Enhanced Host Controller Interface (USB2)</capability>
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="irq" value="19" />
        <resource type="memory" value="c43fd000-c43fd3ff" />
       </resources>
        <node id="usbhost" claimed="true" class="bus" handle="USB:1:1">
         <product>EHCI Host Controller [1D6B:2]</product>
         <vendor>Linux 2.6.32-220.el6.x86_64 ehci_hcd [1D6B]</vendor>
         <physid>1</physid>
         <businfo>usb@1</businfo>
         <logicalname>usb1</logicalname>
         <version>2.06</version>
         <configuration>
          <setting id="driver" value="hub" />
          <setting id="slots" value="3" />
          <setting id="speed" value="480Mbit/s" />
         </configuration>
         <capabilities>
          <capability id="usb-2.00" >USB 2.0</capability>
         </capabilities>
          <node id="usb" claimed="true" class="bus" handle="USB:1:2">
           <description>USB hub</description>
           <product>Integrated Rate Matching Hub [8087:24]</product>
           <vendor>Intel Corp. [8087]</vendor>
           <physid>1</physid>
           <businfo>usb@1:1</businfo>
           <version>0.00</version>
           <configuration>
            <setting id="driver" value="hub" />
            <setting id="slots" value="6" />
            <setting id="speed" value="480Mbit/s" />
           </configuration>
           <capabilities>
            <capability id="usb-2.00" >USB 2.0</capability>
           </capabilities>
          </node>
        </node>
      </node>
      <node id="pci:6" claimed="true" class="bridge" handle="PCIBUS:0000:06">
       <description>PCI bridge</description>
       <product>Patsburg PCI Express Root Port 1 [8086:1D10]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>1c</physid>
       <businfo>pci@0000:00:1c.0</businfo>
       <version>b6</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="pcieport" />
       </configuration>
       <capabilities>
        <capability id="pci" />
        <capability id="pciexpress" >PCI Express</capability>
        <capability id="msi" >Message Signalled Interrupts</capability>
        <capability id="pm" >Power Management</capability>
        <capability id="normal_decode" />
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="irq" value="85" />
        <resource type="ioport" value="3000(size=4096)" />
        <resource type="memory" value="c4500000-c45fffff" />
        <resource type="ioport" value="c4100000(size=1048576)" />
       </resources>
        <node id="network:0" claimed="true" class="network" handle="PCI:0000:06:00.0">
         <description>Ethernet interface</description>
         <product>I350 Gigabit Network Connection [8086:1521]</product>
         <vendor>Intel Corporation [8086]</vendor>
         <physid>0</physid>
         <businfo>pci@0000:06:00.0</businfo>
         <logicalname>eth0</logicalname>
         <version>01</version>
         <serial>40:f2:e9:98:f5:42</serial>
         <size units="bit/s">1000000000</size>
         <capacity>1000000000</capacity>
         <width units="bits">32</width>
         <clock units="Hz">33000000</clock>
         <configuration>
          <setting id="autonegotiation" value="on" />
          <setting id="broadcast" value="yes" />
          <setting id="driver" value="igb" />
          <setting id="driverversion" value="3.0.6-k" />
          <setting id="duplex" value="full" />
          <setting id="firmware" value="1.6-3" />
          <setting id="latency" value="0" />
          <setting id="link" value="yes" />
          <setting id="multicast" value="yes" />
          <setting id="port" value="twisted pair" />
          <setting id="slave" value="yes" />
          <setting id="speed" value="1Gbit/s" />
         </configuration>
         <capabilities>
          <capability id="pm" >Power Management</capability>
          <capability id="msi" >Message Signalled Interrupts</capability>
          <capability id="msix" >MSI-X</capability>
          <capability id="pciexpress" >PCI Express</capability>
          <capability id="bus_master" >bus mastering</capability>
          <capability id="cap_list" >PCI capabilities listing</capability>
          <capability id="ethernet" />
          <capability id="physical" >Physical interface</capability>
          <capability id="tp" >twisted pair</capability>
          <capability id="10bt" >10Mbit/s</capability>
          <capability id="10bt-fd" >10Mbit/s (full duplex)</capability>
          <capability id="100bt" >100Mbit/s</capability>
          <capability id="100bt-fd" >100Mbit/s (full duplex)</capability>
          <capability id="1000bt-fd" >1Gbit/s (full duplex)</capability>
          <capability id="autonegotiation" >Auto-negotiation</capability>
         </capabilities>
         <resources>
          <resource type="irq" value="16" />
          <resource type="memory" value="c4580000-c459ffff" />
          <resource type="ioport" value="3f80(size=32)" />
          <resource type="memory" value="c4570000-c4573fff" />
          <resource type="memory" value="c4100000-c411ffff(prefetchable)" />
          <resource type="memory" value="c4120000-c413ffff(prefetchable)" />
         </resources>
        </node>
        <node id="network:1" claimed="true" class="network" handle="PCI:0000:06:00.1">
         <description>Ethernet interface</description>
         <product>I350 Gigabit Network Connection [8086:1521]</product>
         <vendor>Intel Corporation [8086]</vendor>
         <physid>0.1</physid>
         <businfo>pci@0000:06:00.1</businfo>
         <logicalname>eth1</logicalname>
         <version>01</version>
         <serial>40:f2:e9:98:f5:42</serial>
         <size units="bit/s">1000000000</size>
         <capacity>1000000000</capacity>
         <width units="bits">32</width>
         <clock units="Hz">33000000</clock>
         <configuration>
          <setting id="autonegotiation" value="on" />
          <setting id="broadcast" value="yes" />
          <setting id="driver" value="igb" />
          <setting id="driverversion" value="3.0.6-k" />
          <setting id="duplex" value="full" />
          <setting id="firmware" value="1.6-3" />
          <setting id="latency" value="0" />
          <setting id="link" value="yes" />
          <setting id="multicast" value="yes" />
          <setting id="port" value="twisted pair" />
          <setting id="slave" value="yes" />
          <setting id="speed" value="1Gbit/s" />
         </configuration>
         <capabilities>
          <capability id="pm" >Power Management</capability>
          <capability id="msi" >Message Signalled Interrupts</capability>
          <capability id="msix" >MSI-X</capability>
          <capability id="pciexpress" >PCI Express</capability>
          <capability id="bus_master" >bus mastering</capability>
          <capability id="cap_list" >PCI capabilities listing</capability>
          <capability id="ethernet" />
          <capability id="physical" >Physical interface</capability>
          <capability id="tp" >twisted pair</capability>
          <capability id="10bt" >10Mbit/s</capability>
          <capability id="10bt-fd" >10Mbit/s (full duplex)</capability>
          <capability id="100bt" >100Mbit/s</capability>
          <capability id="100bt-fd" >100Mbit/s (full duplex)</capability>
          <capability id="1000bt-fd" >1Gbit/s (full duplex)</capability>
          <capability id="autonegotiation" >Auto-negotiation</capability>
         </capabilities>
         <resources>
          <resource type="irq" value="17" />
          <resource type="memory" value="c45a0000-c45bffff" />
          <resource type="ioport" value="3fa0(size=32)" />
          <resource type="memory" value="c4574000-c4577fff" />
          <resource type="memory" value="c4140000-c415ffff(prefetchable)" />
          <resource type="memory" value="c4160000-c417ffff(prefetchable)" />
         </resources>
        </node>
        <node id="network:2" disabled="true" claimed="true" class="network" handle="PCI:0000:06:00.2">
         <description>Ethernet interface</description>
         <product>I350 Gigabit Network Connection [8086:1521]</product>
         <vendor>Intel Corporation [8086]</vendor>
         <physid>0.2</physid>
         <businfo>pci@0000:06:00.2</businfo>
         <logicalname>eth2</logicalname>
         <version>01</version>
         <serial>40:f2:e9:98:f5:44</serial>
         <capacity>1000000000</capacity>
         <width units="bits">32</width>
         <clock units="Hz">33000000</clock>
         <configuration>
          <setting id="autonegotiation" value="on" />
          <setting id="broadcast" value="yes" />
          <setting id="driver" value="igb" />
          <setting id="driverversion" value="3.0.6-k" />
          <setting id="firmware" value="1.6-3" />
          <setting id="latency" value="0" />
          <setting id="link" value="no" />
          <setting id="multicast" value="yes" />
          <setting id="port" value="twisted pair" />
         </configuration>
         <capabilities>
          <capability id="pm" >Power Management</capability>
          <capability id="msi" >Message Signalled Interrupts</capability>
          <capability id="msix" >MSI-X</capability>
          <capability id="pciexpress" >PCI Express</capability>
          <capability id="bus_master" >bus mastering</capability>
          <capability id="cap_list" >PCI capabilities listing</capability>
          <capability id="ethernet" />
          <capability id="physical" >Physical interface</capability>
          <capability id="tp" >twisted pair</capability>
          <capability id="10bt" >10Mbit/s</capability>
          <capability id="10bt-fd" >10Mbit/s (full duplex)</capability>
          <capability id="100bt" >100Mbit/s</capability>
          <capability id="100bt-fd" >100Mbit/s (full duplex)</capability>
          <capability id="1000bt-fd" >1Gbit/s (full duplex)</capability>
          <capability id="autonegotiation" >Auto-negotiation</capability>
         </capabilities>
         <resources>
          <resource type="irq" value="18" />
          <resource type="memory" value="c45c0000-c45dffff" />
          <resource type="ioport" value="3fc0(size=32)" />
          <resource type="memory" value="c4578000-c457bfff" />
          <resource type="memory" value="c4180000-c419ffff(prefetchable)" />
          <resource type="memory" value="c41a0000-c41bffff(prefetchable)" />
         </resources>
        </node>
        <node id="network:3" disabled="true" claimed="true" class="network" handle="PCI:0000:06:00.3">
         <description>Ethernet interface</description>
         <product>I350 Gigabit Network Connection [8086:1521]</product>
         <vendor>Intel Corporation [8086]</vendor>
         <physid>0.3</physid>
         <businfo>pci@0000:06:00.3</businfo>
         <logicalname>eth3</logicalname>
         <version>01</version>
         <serial>40:f2:e9:98:f5:45</serial>
         <capacity>1000000000</capacity>
         <width units="bits">32</width>
         <clock units="Hz">33000000</clock>
         <configuration>
          <setting id="autonegotiation" value="on" />
          <setting id="broadcast" value="yes" />
          <setting id="driver" value="igb" />
          <setting id="driverversion" value="3.0.6-k" />
          <setting id="firmware" value="1.6-3" />
          <setting id="latency" value="0" />
          <setting id="link" value="no" />
          <setting id="multicast" value="yes" />
          <setting id="port" value="twisted pair" />
         </configuration>
         <capabilities>
          <capability id="pm" >Power Management</capability>
          <capability id="msi" >Message Signalled Interrupts</capability>
          <capability id="msix" >MSI-X</capability>
          <capability id="pciexpress" >PCI Express</capability>
          <capability id="bus_master" >bus mastering</capability>
          <capability id="cap_list" >PCI capabilities listing</capability>
          <capability id="ethernet" />
          <capability id="physical" >Physical interface</capability>
          <capability id="tp" >twisted pair</capability>
          <capability id="10bt" >10Mbit/s</capability>
          <capability id="10bt-fd" >10Mbit/s (full duplex)</capability>
          <capability id="100bt" >100Mbit/s</capability>
          <capability id="100bt-fd" >100Mbit/s (full duplex)</capability>
          <capability id="1000bt-fd" >1Gbit/s (full duplex)</capability>
          <capability id="autonegotiation" >Auto-negotiation</capability>
         </capabilities>
         <resources>
          <resource type="irq" value="19" />
          <resource type="memory" value="c45e0000-c45fffff" />
          <resource type="ioport" value="3fe0(size=32)" />
          <resource type="memory" value="c457c000-c457ffff" />
          <resource type="memory" value="c41c0000-c41dffff(prefetchable)" />
          <resource type="memory" value="c41e0000-c41fffff(prefetchable)" />
         </resources>
        </node>
      </node>
      <node id="pci:7" claimed="true" class="bridge" handle="PCIBUS:0000:01">
       <description>PCI bridge</description>
       <product>Patsburg PCI Express Root Port 8 [8086:1D1E]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>1c.7</physid>
       <businfo>pci@0000:00:1c.7</businfo>
       <version>b6</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="pcieport" />
       </configuration>
       <capabilities>
        <capability id="pci" />
        <capability id="pciexpress" >PCI Express</capability>
        <capability id="msi" >Message Signalled Interrupts</capability>
        <capability id="pm" >Power Management</capability>
        <capability id="normal_decode" />
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="irq" value="86" />
        <resource type="memory" value="c4600000-c4ffffff" />
        <resource type="ioport" value="c5000000(size=16777216)" />
       </resources>
        <node id="pci" claimed="true" class="bridge" handle="PCIBUS:0000:02">
         <description>PCI bridge</description>
         <product>SH7757 PCIe Switch [PS] [1912:13]</product>
         <vendor>Renesas Technology Corp. [1912]</vendor>
         <physid>0</physid>
         <businfo>pci@0000:01:00.0</businfo>
         <version>00</version>
         <width units="bits">32</width>
         <clock units="Hz">33000000</clock>
         <capabilities>
          <capability id="pci" />
          <capability id="pm" >Power Management</capability>
          <capability id="msi" >Message Signalled Interrupts</capability>
          <capability id="pciexpress" >PCI Express</capability>
          <capability id="normal_decode" />
          <capability id="bus_master" >bus mastering</capability>
          <capability id="cap_list" >PCI capabilities listing</capability>
         </capabilities>
         <resources>
          <resource type="memory" value="c4600000-c4ffffff" />
          <resource type="ioport" value="c5000000(size=16777216)" />
         </resources>
          <node id="pci:0" claimed="true" class="bridge" handle="PCIBUS:0000:03">
           <description>PCI bridge</description>
           <product>SH7757 PCIe Switch [PS] [1912:13]</product>
           <vendor>Renesas Technology Corp. [1912]</vendor>
           <physid>0</physid>
           <businfo>pci@0000:02:00.0</businfo>
           <version>00</version>
           <width units="bits">32</width>
           <clock units="Hz">33000000</clock>
           <capabilities>
            <capability id="pci" />
            <capability id="pm" >Power Management</capability>
            <capability id="msi" >Message Signalled Interrupts</capability>
            <capability id="pciexpress" >PCI Express</capability>
            <capability id="normal_decode" />
            <capability id="bus_master" >bus mastering</capability>
            <capability id="cap_list" >PCI capabilities listing</capability>
           </capabilities>
           <resources>
            <resource type="memory" value="c4700000-c4ffffff" />
            <resource type="ioport" value="c5000000(size=16777216)" />
           </resources>
            <node id="pci" claimed="true" class="bridge" handle="PCIBUS:0000:04">
             <description>PCI bridge</description>
             <product>SH7757 PCIe-PCI Bridge [PPB] [1912:12]</product>
             <vendor>Renesas Technology Corp. [1912]</vendor>
             <physid>0</physid>
             <businfo>pci@0000:03:00.0</businfo>
             <version>00</version>
             <width units="bits">32</width>
             <clock units="Hz">33000000</clock>
             <capabilities>
              <capability id="pci" />
              <capability id="pm" >Power Management</capability>
              <capability id="msi" >Message Signalled Interrupts</capability>
              <capability id="pciexpress" >PCI Express</capability>
              <capability id="normal_decode" />
              <capability id="bus_master" >bus mastering</capability>
              <capability id="cap_list" >PCI capabilities listing</capability>
             </capabilities>
             <resources>
              <resource type="memory" value="c4700000-c4ffffff" />
              <resource type="ioport" value="c5000000(size=16777216)" />
             </resources>
              <node id="display" class="display" handle="PCI:0000:04:00.0">
               <description>VGA compatible controller</description>
               <product>G200eR2 [102B:534]</product>
               <vendor>Matrox Graphics, Inc. [102B]</vendor>
               <physid>0</physid>
               <businfo>pci@0000:04:00.0</businfo>
               <version>00</version>
               <width units="bits">32</width>
               <clock units="Hz">33000000</clock>
               <configuration>
                <setting id="latency" value="64" />
                <setting id="maxlatency" value="32" />
                <setting id="mingnt" value="16" />
               </configuration>
               <capabilities>
                <capability id="pm" >Power Management</capability>
                <capability id="vga_controller" />
                <capability id="bus_master" >bus mastering</capability>
                <capability id="cap_list" >PCI capabilities listing</capability>
               </capabilities>
               <resources>
                <resource type="memory" value="c5000000-c5ffffff(prefetchable)" />
                <resource type="memory" value="c47fc000-c47fffff" />
                <resource type="memory" value="c4800000-c4ffffff" />
               </resources>
              </node>
            </node>
          </node>
          <node id="pci:1" claimed="true" class="bridge" handle="PCIBUS:0000:05">
           <description>PCI bridge</description>
           <product>SH7757 PCIe Switch [PS] [1912:13]</product>
           <vendor>Renesas Technology Corp. [1912]</vendor>
           <physid>1</physid>
           <businfo>pci@0000:02:01.0</businfo>
           <version>00</version>
           <width units="bits">32</width>
           <clock units="Hz">33000000</clock>
           <capabilities>
            <capability id="pci" />
            <capability id="pm" >Power Management</capability>
            <capability id="msi" >Message Signalled Interrupts</capability>
            <capability id="pciexpress" >PCI Express</capability>
            <capability id="normal_decode" />
            <capability id="bus_master" >bus mastering</capability>
            <capability id="cap_list" >PCI capabilities listing</capability>
           </capabilities>
           <resources>
            <resource type="memory" value="c4600000-c46fffff" />
           </resources>
          </node>
        </node>
      </node>
      <node id="usb:1" claimed="true" class="bus" handle="PCI:0000:00:1d.0">
       <description>USB controller</description>
       <product>Patsburg USB2 Enhanced Host Controller #1 [8086:1D26]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>1d</physid>
       <businfo>pci@0000:00:1d.0</businfo>
       <version>06</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="ehci_hcd" />
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="pm" >Power Management</capability>
        <capability id="debug" >Debug port</capability>
        <capability id="ehci" >Enhanced Host Controller Interface (USB2)</capability>
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="irq" value="23" />
        <resource type="memory" value="c43fe000-c43fe3ff" />
       </resources>
        <node id="usbhost" claimed="true" class="bus" handle="USB:2:1">
         <product>EHCI Host Controller [1D6B:2]</product>
         <vendor>Linux 2.6.32-220.el6.x86_64 ehci_hcd [1D6B]</vendor>
         <physid>1</physid>
         <businfo>usb@2</businfo>
         <logicalname>usb2</logicalname>
         <version>2.06</version>
         <configuration>
          <setting id="driver" value="hub" />
          <setting id="slots" value="3" />
          <setting id="speed" value="480Mbit/s" />
         </configuration>
         <capabilities>
          <capability id="usb-2.00" >USB 2.0</capability>
         </capabilities>
          <node id="usb" claimed="true" class="bus" handle="USB:2:2">
           <description>USB hub</description>
           <product>Integrated Rate Matching Hub [8087:24]</product>
           <vendor>Intel Corp. [8087]</vendor>
           <physid>1</physid>
           <businfo>usb@2:1</businfo>
           <version>0.00</version>
           <configuration>
            <setting id="driver" value="hub" />
            <setting id="slots" value="8" />
            <setting id="speed" value="480Mbit/s" />
           </configuration>
           <capabilities>
            <capability id="usb-2.00" >USB 2.0</capability>
           </capabilities>
            <node id="usb" claimed="true" class="bus" handle="USB:2:3">
             <description>USB hub</description>
             <product>Gadget USB HUB [FFFF:248]</product>
             <vendor>no manufacturer [FFFF]</vendor>
             <physid>1</physid>
             <businfo>usb@2:1.1</businfo>
             <version>0.00</version>
             <serial>0123456789</serial>
             <configuration>
              <setting id="driver" value="hub" />
              <setting id="maxpower" value="100mA" />
              <setting id="slots" value="6" />
              <setting id="speed" value="480Mbit/s" />
             </configuration>
             <capabilities>
              <capability id="usb-2.00" >USB 2.0</capability>
             </capabilities>
              <node id="usb" claimed="true" class="communication" handle="USB:2:5">
               <description>Communication device</description>
               <product>RNDIS/Ethernet Gadget [4B3:4010]</product>
               <vendor>IBM [4B3]</vendor>
               <physid>5</physid>
               <businfo>usb@2:1.1.5</businfo>
               <version>3.25</version>
               <configuration>
                <setting id="driver" value="cdc_ether" />
                <setting id="maxpower" value="2mA" />
                <setting id="speed" value="480Mbit/s" />
               </configuration>
               <capabilities>
                <capability id="usb-2.00" >USB 2.0</capability>
               </capabilities>
              </node>
            </node>
          </node>
        </node>
      </node>
      <node id="pci:8" claimed="true" class="bridge" handle="PCIBUS:0000:26">
       <description>PCI bridge</description>
       <product>82801 PCI Bridge [8086:244E]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>1e</physid>
       <businfo>pci@0000:00:1e.0</businfo>
       <version>a6</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <capabilities>
        <capability id="pci" />
        <capability id="subtractive_decode" />
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
      </node>
      <node id="isa" claimed="true" class="bridge" handle="PCI:0000:00:1f.0">
       <description>ISA bridge</description>
       <product>Patsburg LPC Controller [8086:1D41]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>1f</physid>
       <businfo>pci@0000:00:1f.0</businfo>
       <version>06</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="isa" />
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
      </node>
      <node id="serial" claimed="true" class="bus" handle="PCI:0000:00:1f.3">
       <description>SMBus</description>
       <product>Patsburg SMBus Host Controller [8086:1D22]</product>
       <vendor>Intel Corporation [8086]</vendor>
       <physid>1f.3</physid>
       <businfo>pci@0000:00:1f.3</businfo>
       <version>06</version>
       <width units="bits">64</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="i801_smbus" />
        <setting id="latency" value="0" />
       </configuration>
       <resources>
        <resource type="irq" value="11" />
        <resource type="memory" value="c40de000-c40de0ff" />
        <resource type="ioport" value="1fe0(size=32)" />
       </resources>
      </node>
    </node>
    <node id="pci:1" claimed="true" class="bridge" handle="PCIBUS:0000:81">
     <description>PCI bridge</description>
     <product>Intel Corporation [8086:E01]</product>
     <vendor>Intel Corporation [8086]</vendor>
     <physid>0</physid>
     <businfo>pci@0000:80:00.0</businfo>
     <version>04</version>
     <width units="bits">32</width>
     <clock units="Hz">33000000</clock>
     <configuration>
      <setting id="driver" value="pcieport" />
     </configuration>
     <capabilities>
      <capability id="pci" />
      <capability id="msi" >Message Signalled Interrupts</capability>
      <capability id="pciexpress" >PCI Express</capability>
      <capability id="pm" >Power Management</capability>
      <capability id="normal_decode" />
      <capability id="bus_master" >bus mastering</capability>
      <capability id="cap_list" >PCI capabilities listing</capability>
     </capabilities>
     <resources>
      <resource type="irq" value="87" />
     </resources>
    </node>
    <node id="pci:2" claimed="true" class="bridge" handle="PCIBUS:0000:86">
     <description>PCI bridge</description>
     <product>Intel Corporation [8086:E04]</product>
     <vendor>Intel Corporation [8086]</vendor>
     <physid>101</physid>
     <businfo>pci@0000:80:02.0</businfo>
     <version>04</version>
     <width units="bits">32</width>
     <clock units="Hz">33000000</clock>
     <configuration>
      <setting id="driver" value="pcieport" />
     </configuration>
     <capabilities>
      <capability id="pci" />
      <capability id="msi" >Message Signalled Interrupts</capability>
      <capability id="pciexpress" >PCI Express</capability>
      <capability id="pm" >Power Management</capability>
      <capability id="normal_decode" />
      <capability id="bus_master" >bus mastering</capability>
      <capability id="cap_list" >PCI capabilities listing</capability>
     </capabilities>
     <resources>
      <resource type="irq" value="88" />
     </resources>
    </node>
    <node id="pci:3" claimed="true" class="bridge" handle="PCIBUS:0000:8b">
     <description>PCI bridge</description>
     <product>Intel Corporation [8086:E06]</product>
     <vendor>Intel Corporation [8086]</vendor>
     <physid>2.2</physid>
     <businfo>pci@0000:80:02.2</businfo>
     <version>04</version>
     <width units="bits">32</width>
     <clock units="Hz">33000000</clock>
     <configuration>
      <setting id="driver" value="pcieport" />
     </configuration>
     <capabilities>
      <capability id="pci" />
      <capability id="msi" >Message Signalled Interrupts</capability>
      <capability id="pciexpress" >PCI Express</capability>
      <capability id="pm" >Power Management</capability>
      <capability id="normal_decode" />
      <capability id="bus_master" >bus mastering</capability>
      <capability id="cap_list" >PCI capabilities listing</capability>
     </capabilities>
     <resources>
      <resource type="irq" value="89" />
     </resources>
    </node>
    <node id="pci:4" claimed="true" class="bridge" handle="PCIBUS:0000:90">
     <description>PCI bridge</description>
     <product>Intel Corporation [8086:E08]</product>
     <vendor>Intel Corporation [8086]</vendor>
     <physid>3</physid>
     <businfo>pci@0000:80:03.0</businfo>
     <version>04</version>
     <width units="bits">32</width>
     <clock units="Hz">33000000</clock>
     <configuration>
      <setting id="driver" value="pcieport" />
     </configuration>
     <capabilities>
      <capability id="pci" />
      <capability id="msi" >Message Signalled Interrupts</capability>
      <capability id="pciexpress" >PCI Express</capability>
      <capability id="pm" >Power Management</capability>
      <capability id="normal_decode" />
      <capability id="bus_master" >bus mastering</capability>
      <capability id="cap_list" >PCI capabilities listing</capability>
     </capabilities>
     <resources>
      <resource type="irq" value="90" />
     </resources>
    </node>
    <node id="generic:0" class="generic" handle="PCI:0000:80:04.0">
     <description>System peripheral</description>
     <product>Intel Corporation [8086:E20]</product>
     <vendor>Intel Corporation [8086]</vendor>
     <physid>4</physid>
     <businfo>pci@0000:80:04.0</businfo>
     <version>04</version>
     <width units="bits">64</width>
     <clock units="Hz">33000000</clock>
     <configuration>
      <setting id="latency" value="0" />
     </configuration>
     <capabilities>
      <capability id="msix" >MSI-X</capability>
      <capability id="pciexpress" >PCI Express</capability>
      <capability id="pm" >Power Management</capability>
      <capability id="bus_master" >bus mastering</capability>
      <capability id="cap_list" >PCI capabilities listing</capability>
     </capabilities>
     <resources>
      <resource type="memory" value="90000000-90003fff" />
     </resources>
    </node>
    <node id="generic:1" class="generic" handle="PCI:0000:80:04.1">
     <description>System peripheral</description>
     <product>Intel Corporation [8086:E21]</product>
     <vendor>Intel Corporation [8086]</vendor>
     <physid>4.1</physid>
     <businfo>pci@0000:80:04.1</businfo>
     <version>04</version>
     <width units="bits">64</width>
     <clock units="Hz">33000000</clock>
     <configuration>
      <setting id="latency" value="0" />
     </configuration>
     <capabilities>
      <capability id="msix" >MSI-X</capability>
      <capability id="pciexpress" >PCI Express</capability>
      <capability id="pm" >Power Management</capability>
      <capability id="bus_master" >bus mastering</capability>
      <capability id="cap_list" >PCI capabilities listing</capability>
     </capabilities>
     <resources>
      <resource type="memory" value="90004000-90007fff" />
     </resources>
    </node>
    <node id="generic:2" class="generic" handle="PCI:0000:80:04.2">
     <description>System peripheral</description>
     <product>Intel Corporation [8086:E22]</product>
     <vendor>Intel Corporation [8086]</vendor>
     <physid>4.2</physid>
     <businfo>pci@0000:80:04.2</businfo>
     <version>04</version>
     <width units="bits">64</width>
     <clock units="Hz">33000000</clock>
     <configuration>
      <setting id="latency" value="0" />
     </configuration>
     <capabilities>
      <capability id="msix" >MSI-X</capability>
      <capability id="pciexpress" >PCI Express</capability>
      <capability id="pm" >Power Management</capability>
      <capability id="bus_master" >bus mastering</capability>
      <capability id="cap_list" >PCI capabilities listing</capability>
     </capabilities>
     <resources>
      <resource type="memory" value="90008000-9000bfff" />
     </resources>
    </node>
    <node id="generic:3" class="generic" handle="PCI:0000:80:04.3">
     <description>System peripheral</description>
     <product>Intel Corporation [8086:E23]</product>
     <vendor>Intel Corporation [8086]</vendor>
     <physid>4.3</physid>
     <businfo>pci@0000:80:04.3</businfo>
     <version>04</version>
     <width units="bits">64</width>
     <clock units="Hz">33000000</clock>
     <configuration>
      <setting id="latency" value="0" />
     </configuration>
     <capabilities>
      <capability id="msix" >MSI-X</capability>
      <capability id="pciexpress" >PCI Express</capability>
      <capability id="pm" >Power Management</capability>
      <capability id="bus_master" >bus mastering</capability>
      <capability id="cap_list" >PCI capabilities listing</capability>
     </capabilities>
     <resources>
      <resource type="memory" value="9000c000-9000ffff" />
     </resources>
    </node>
    <node id="generic:4" class="generic" handle="PCI:0000:80:04.4">
     <description>System peripheral</description>
     <product>Intel Corporation [8086:E24]</product>
     <vendor>Intel Corporation [8086]</vendor>
     <physid>4.4</physid>
     <businfo>pci@0000:80:04.4</businfo>
     <version>04</version>
     <width units="bits">64</width>
     <clock units="Hz">33000000</clock>
     <configuration>
      <setting id="latency" value="0" />
     </configuration>
     <capabilities>
      <capability id="msix" >MSI-X</capability>
      <capability id="pciexpress" >PCI Express</capability>
      <capability id="pm" >Power Management</capability>
      <capability id="bus_master" >bus mastering</capability>
      <capability id="cap_list" >PCI capabilities listing</capability>
     </capabilities>
     <resources>
      <resource type="memory" value="90010000-90013fff" />
     </resources>
    </node>
    <node id="generic:5" class="generic" handle="PCI:0000:80:04.5">
     <description>System peripheral</description>
     <product>Intel Corporation [8086:E25]</product>
     <vendor>Intel Corporation [8086]</vendor>
     <physid>4.5</physid>
     <businfo>pci@0000:80:04.5</businfo>
     <version>04</version>
     <width units="bits">64</width>
     <clock units="Hz">33000000</clock>
     <configuration>
      <setting id="latency" value="0" />
     </configuration>
     <capabilities>
      <capability id="msix" >MSI-X</capability>
      <capability id="pciexpress" >PCI Express</capability>
      <capability id="pm" >Power Management</capability>
      <capability id="bus_master" >bus mastering</capability>
      <capability id="cap_list" >PCI capabilities listing</capability>
     </capabilities>
     <resources>
      <resource type="memory" value="90014000-90017fff" />
     </resources>
    </node>
    <node id="generic:6" class="generic" handle="PCI:0000:80:04.6">
     <description>System peripheral</description>
     <product>Intel Corporation [8086:E26]</product>
     <vendor>Intel Corporation [8086]</vendor>
     <physid>4.6</physid>
     <businfo>pci@0000:80:04.6</businfo>
     <version>04</version>
     <width units="bits">64</width>
     <clock units="Hz">33000000</clock>
     <configuration>
      <setting id="latency" value="0" />
     </configuration>
     <capabilities>
      <capability id="msix" >MSI-X</capability>
      <capability id="pciexpress" >PCI Express</capability>
      <capability id="pm" >Power Management</capability>
      <capability id="bus_master" >bus mastering</capability>
      <capability id="cap_list" >PCI capabilities listing</capability>
     </capabilities>
     <resources>
      <resource type="memory" value="90018000-9001bfff" />
     </resources>
    </node>
    <node id="generic:7" class="generic" handle="PCI:0000:80:04.7">
     <description>System peripheral</description>
     <product>Intel Corporation [8086:E27]</product>
     <vendor>Intel Corporation [8086]</vendor>
     <physid>4.7</physid>
     <businfo>pci@0000:80:04.7</businfo>
     <version>04</version>
     <width units="bits">64</width>
     <clock units="Hz">33000000</clock>
     <configuration>
      <setting id="latency" value="0" />
     </configuration>
     <capabilities>
      <capability id="msix" >MSI-X</capability>
      <capability id="pciexpress" >PCI Express</capability>
      <capability id="pm" >Power Management</capability>
      <capability id="bus_master" >bus mastering</capability>
      <capability id="cap_list" >PCI capabilities listing</capability>
     </capabilities>
     <resources>
      <resource type="memory" value="9001c000-9001ffff" />
     </resources>
    </node>
    <node id="generic:8" class="generic" handle="PCI:0000:80:05.0">
     <description>System peripheral</description>
     <product>Intel Corporation [8086:E28]</product>
     <vendor>Intel Corporation [8086]</vendor>
     <physid>5</physid>
     <businfo>pci@0000:80:05.0</businfo>
     <version>04</version>
     <width units="bits">32</width>
     <clock units="Hz">33000000</clock>
     <configuration>
      <setting id="latency" value="0" />
     </configuration>
     <capabilities>
      <capability id="pciexpress" >PCI Express</capability>
      <capability id="cap_list" >PCI capabilities listing</capability>
     </capabilities>
    </node>
    <node id="generic:9" class="generic" handle="PCI:0000:80:05.2">
     <description>System peripheral</description>
     <product>Intel Corporation [8086:E2A]</product>
     <vendor>Intel Corporation [8086]</vendor>
     <physid>5.2</physid>
     <businfo>pci@0000:80:05.2</businfo>
     <version>04</version>
     <width units="bits">32</width>
     <clock units="Hz">33000000</clock>
     <configuration>
      <setting id="latency" value="0" />
     </configuration>
     <capabilities>
      <capability id="pciexpress" >PCI Express</capability>
      <capability id="cap_list" >PCI capabilities listing</capability>
     </capabilities>
    </node>
  </node>
  <node id="network:0" disabled="true" claimed="true" class="network" handle="">
   <description>Ethernet interface</description>
   <physid>1</physid>
   <logicalname>usb0</logicalname>
   <serial>42:f2:e9:98:f5:41</serial>
   <configuration>
    <setting id="broadcast" value="yes" />
    <setting id="driver" value="cdc_ether" />
    <setting id="driverversion" value="22-Aug-2005" />
    <setting id="firmware" value="CDC Ethernet Device" />
    <setting id="link" value="yes" />
    <setting id="multicast" value="yes" />
   </configuration>
   <capabilities>
    <capability id="ethernet" />
    <capability id="physical" >Physical interface</capability>
   </capabilities>
  </node>
  <node id="network:1" claimed="true" class="network" handle="">
   <description>Ethernet interface</description>
   <physid>2</physid>
   <logicalname>bond0</logicalname>
   <serial>40:f2:e9:98:f5:42</serial>
   <configuration>
    <setting id="broadcast" value="yes" />
    <setting id="driver" value="bonding" />
    <setting id="driverversion" value="3.6.0" />
    <setting id="firmware" value="2" />
    <setting id="ip" value="172.16.1.42" />
    <setting id="link" value="yes" />
    <setting id="master" value="yes" />
    <setting id="multicast" value="yes" />
   </configuration>
   <capabilities>
    <capability id="ethernet" />
    <capability id="physical" >Physical interface</capability>
   </capabilities>
  </node>
</node>
</list>

    ''')

from pprint import pprint
pprint(xml2dict.etree_to_dict(e))

